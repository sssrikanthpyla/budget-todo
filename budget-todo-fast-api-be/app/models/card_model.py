from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database_configure import Base

class Card(Base):
    __tablename__ = "credit_card_details"
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String(length=30), unique=True, nullable=False)
    name_of_card = Column(String(length=50), index=True, nullable=False)
    card_title = Column(String(length=20), index=True, nullable=False)
    bill_generation_date = Column(Date, index=True)
    payment_due_date = Column(Date, index=True)
    payment_completed_date = Column(Date, index=True)
    is_payment_completed = Column(Boolean, index=True)
    is_bill_generated = Column(Boolean, index=True)
    user_id = Column(Integer, ForeignKey("master_data.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="cards")
