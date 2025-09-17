from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models

router = APIRouter()

@router.post('/')
def create_sale(payload: dict, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == payload.get('product_id')).first()
    if not product:
        return {"error": "product not found"}
    unit_price = float(product.price_sale)
    total_price = unit_price * int(payload.get('quantity', 1))
    sale = models.Sale(product_id=product.id, client_id=payload.get('client_id'), quantity=payload.get('quantity'), unit_price=unit_price, total_price=total_price)
    db.add(sale)
    stock = db.query(models.Stock).filter(models.Stock.product_id == product.id).first()
    if stock:
        stock.quantity = max(0, stock.quantity - int(payload.get('quantity', 1)))
    db.commit()
    return {"ok": True, "sale_id": sale.id}
