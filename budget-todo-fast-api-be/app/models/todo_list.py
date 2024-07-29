from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database_configure import Base

class TodoList(Base):
    __tablename__ = "todo_list"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=30), unique=True, nullable=False)
    purpose = Column(String(length=50), index=True)
    description = Column(String(length=200), index=True)
    priority = Column(String(length=20))
    user_id = Column(Integer, ForeignKey("master_data.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="todolists")
