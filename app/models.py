from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    #modelo de usuário
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    is_active = Column(Boolean, default=True)



    #representação do usuário
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
