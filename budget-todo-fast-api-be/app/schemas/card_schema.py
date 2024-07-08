from pydantic import BaseModel
from datetime import date

class CardBase(BaseModel):
    card_number: int
    name_of_card: str
    expire_date: date
    valid_through: date
    payment_generation_date: date
    payment_due_date: date
    payment_completed_date: date
    is_payment_completed: bool
    is_bill_generated: bool

class CardCreate(CardBase):
    pass

class CardUpdate(CardBase):
    pass

class Card(CardBase):
    id: int
    
    class Config:
        orm_mode = True

    