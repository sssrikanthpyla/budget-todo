from pydantic import BaseModel
from datetime import date

class KeynotesBase(BaseModel):
    name: str
    purpose: str
    description: str
    star: str

class KeynotesCreate(KeynotesBase):
    user_id: int

class KeynotesUpdate(KeynotesBase):
    pass

class Keynotes(KeynotesBase):
    id: int
    
    class Config:
        orm_mode = True

    