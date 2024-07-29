from pydantic import BaseModel
from datetime import date

class TodoListBase(BaseModel):
    name: str
    purpose: str
    purpose: str
    description: str
    priority: str

class TodoListCreate(TodoListBase):
    user_id: int

class TodoListUpdate(TodoListBase):
    pass

class TodoList(TodoListBase):
    id: int
    
    class Config:
        orm_mode = True

    