from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database_configure import Base

class Keynotes(Base):
    __tablename__ = "key_notes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=30), unique=True, nullable=False)
    purpose = Column(String(length=50), index=True)
    description = Column(String(length=200), index=True)
    star = Column(String(length=5))
    user_id = Column(Integer, ForeignKey("master_data.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="keynotes")
