from app.config.database_configure import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class SubTask(Base):
    __tablename__ = "sub_tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    due_date = Column(Date)
    is_completed = Column(Boolean, default=False)
    todo_id = Column(Integer, ForeignKey("todos.id"))
    todo = relationship("Todo", back_populates="sub_tasks")

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    due_date = Column(Date)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    is_dependency = Column(Boolean, default=False)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("master_data.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="todolists")
    sub_tasks = relationship("SubTask", back_populates="todo")