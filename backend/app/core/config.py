import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgresql://lojinha:lojinha123@db:5432/lojinha')
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'change-me')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = 'HS256'

settings = Settings()
