from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    email: str
    username: str
    nickname: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True
