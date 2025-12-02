from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

#schemas para criar usuarios

class UserCreate(BaseModel):
    email: EmailStr
    password: str

#Schema para login de usuarios
class UserLogin(BaseModel):
    email: EmailStr
    password: str

#Schema para resposta de usuarios
class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"

