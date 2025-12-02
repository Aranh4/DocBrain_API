from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    #configurações do ambiente

    #openai
    openai_api_key: str

    #jwt
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 120

    #db
    database_url: str = "sqlite:///./db.sqlite3"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings = Settings()