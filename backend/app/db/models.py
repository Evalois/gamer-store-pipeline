from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, JSON
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    contact_info = Column(JSON)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(64), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    price_cost = Column(Numeric(12,2))
    price_sale = Column(Numeric(12,2))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, default=0)
    safety_stock = Column(Integer, default=0)
    reorder_point = Column(Integer, default=0)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(12,2), nullable=False)
    total_price = Column(Numeric(12,2), nullable=False)
    sale_date = Column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(32), default='vendedor')

class AuditLog(Base):
    __tablename__ = 'audit_log'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    action = Column(String(64))
    resource = Column(String(128))
    details = Column(JSON)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
