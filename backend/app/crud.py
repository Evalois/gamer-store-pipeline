from sqlalchemy.orm import Session
from app.db import models
from app.schemas import ProductCreate
from app.security import get_password_hash, verify_password

# Products
def create_product(db: Session, product: ProductCreate):
    db_product = models.Product(sku=product.sku, name=product.name, price_cost=product.price_cost, price_sale=product.price_sale, category_id=product.category_id, supplier_id=product.supplier_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

# Users
def create_user(db: Session, username: str, email: str, password: str, role: str = 'vendedor'):
    hashed = get_password_hash(password)
    user = models.User(username=username, email=email, password_hash=hashed, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user
