from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    sku: str
    name: str
    price_cost: float
    price_sale: float

class ProductCreate(ProductBase):
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None

class ProductRead(ProductBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    username: str
    email: Optional[str]
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    role: str
    class Config:
        orm_mode = True
