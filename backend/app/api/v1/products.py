from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app import crud
from app.schemas import ProductCreate, ProductRead

router = APIRouter()

@router.post('/', response_model=ProductRead)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, payload)

@router.get('/', response_model=List[ProductRead])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@router.get('/{product_id}', response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    p = crud.get_product(db, product_id)
    if not p:
        raise HTTPException(status_code=404, detail='Product not found')
    return p

@router.delete('/{product_id}')
def delete_product(product_id: int, db: Session = Depends(get_db)):
    p = crud.get_product(db, product_id)
    if not p:
        raise HTTPException(status_code=404, detail='Product not found')
    db.delete(p)
    db.commit()
    return {"ok": True}
