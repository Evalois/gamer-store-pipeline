from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db, engine
from app import crud
from app.schemas import Token, UserRead, UserCreate
from app.security import create_access_token

router = APIRouter()

@router.post('/signup', response_model=UserRead)
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    user = crud.create_user(db, payload.username, payload.email or '', payload.password, role='admin')
    return user

@router.post('/token', response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = create_access_token({"sub": user.username, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}
