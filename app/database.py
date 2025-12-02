from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}
)

#session local para criar sessões de conexão com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base para criar modelos de banco de dados

Base = declarative_base()

#função para obter uma sessão do banco de dados
def get_db():
    #Dependencia do FastAPI
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
