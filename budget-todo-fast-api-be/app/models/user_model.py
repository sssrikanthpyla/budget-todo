from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database_configure import Base

class User(Base):
    __tablename__ = "master_data"
    id = Column(Integer, primary_key=True, index=True)
    email=Column(String(length=50), unique=True, nullable=False)
    username=Column(String(length=30), nullable=False)
    nickname=Column(String(length=30), nullable=False)
    cards = relationship("Card", back_populates="user", cascade="all, delete-orphan")
    