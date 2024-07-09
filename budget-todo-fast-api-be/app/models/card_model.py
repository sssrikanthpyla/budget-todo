from sqlalchemy import Column, Integer, String, Date, Boolean
from app.database.database_configure import Base

class Card(Base):
    __tablename__ = "credit_card_details"
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(Integer, unique=True, nullable=False)
    name_of_card = Column(String(length=50), index=True)
    bill_generation_date = Column(Date, index=True)
    payment_due_date = Column(Date, index=True)
    payment_completed_date = Column(Date, index=True)
    is_payment_completed = Column(Boolean, index=True)
    is_bill_generated = Column(Boolean, index=True)
