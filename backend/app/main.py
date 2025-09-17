from fastapi import FastAPI
from app.api.v1 import products, sales, auth
from app.db import models
from app.db.session import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Lojinha Gamer - API')

app.include_router(auth.router, prefix='/api/v1/auth', tags=['auth'])
app.include_router(products.router, prefix='/api/v1/products', tags=['products'])
app.include_router(sales.router, prefix='/api/v1/sales', tags=['sales'])

@app.get('/')
def root():
    return {'ok': True, 'service': 'lojinha-gamer api'}

from app.api.v1 import inference
app.include_router(inference.router, prefix='/api/v1/ml', tags=['ml'])
