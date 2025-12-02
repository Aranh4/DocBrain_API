from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db, engine, Base
from app.models import User
from app.schemas import UserCreate, UserLogin, UserResponse, Token
from app.auth.utils import get_password_hash, verify_password, create_access_token
from app.auth.dependencies import get_current_user
from datetime import timedelta
from app.config import settings



#create if not exists
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DocBrain API",
    description="API para chat com documentos PDF utilizando RAG (Retrieval-Augmented Generation), LangChain e OpenAI.",
    version="0.1.0",
)

@app.get("/")
async def root():
    """Rotad de teste"""
    return {"message": "API está funcionando"}

@app.post("/auth/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    """Registro de novo usuário"""
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já em uso")
    
    #cria hash da senha
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()

    db.refresh(new_user)

    return new_user


@app.post("/auth/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login de usuário retornando token JWT"""
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

    #cria token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.id},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/auth/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Rota protegida: retorna os dados do usuário logado"""
    return current_user

