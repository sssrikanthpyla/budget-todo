from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date

class SubTaskBase(BaseModel):
    title: str
    description: Optional[str]
    due_date: Optional[date]
    is_completed: bool = False

class SubTaskCreate(SubTaskBase):
    id: int
    pass

class SubTask(SubTaskBase):
    id: int

class TodoBase(BaseModel):
    title: str
    description: Optional[str]
    due_date: Optional[date]
    is_dependency: bool = False
    is_completed: bool = False

class TodoCreate(TodoBase):
    user_id: int
    sub_tasks: List[SubTaskCreate] = []

class TodoUpdate(TodoBase):
    sub_tasks: Optional[List[SubTaskCreate]] = None

class Todo(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    sub_tasks: List[SubTask] = []

    class Config:
        from_attributes = True
