from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database_configure import Base
from sqlalchemy.sql import func


class CreditCard(Base):
    __tablename__ = "credit_cards"
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String(16), unique=True)
    card_type = Column(String(length=10))
    card_name = Column(String(length=30))
    card_issued_by = Column(String(length=30))
    cardholder_name = Column(String(30))
    expiry_date = Column(Date)
    cvv = Column(String(3))
    user_id = Column(Integer, ForeignKey("master_data.id"))
    user = relationship("User", back_populates="credit_cards")
    credit_transactions = relationship("CreditTransaction", back_populates="credit_card", cascade="all, delete-orphan")
    credit_bills = relationship("Bill", back_populates="credit_card", cascade="all, delete-orphan")
    creditcard_payments = relationship("CreditCardPaymentDetails", back_populates="credit_card", cascade="all, delete-orphan")


class CreditTransaction(Base):
    __tablename__ = "credit_transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    transaction_date = Column(DateTime)
    description = Column(String(255))
    credit_card_id = Column(Integer, ForeignKey("credit_cards.id", ondelete="CASCADE"))
    credit_card = relationship("CreditCard", back_populates="credit_transactions")

   
class Bill(Base):
    __tablename__ = "credit_bills"
    id = Column(Integer, primary_key=True, index=True)
    bill_due_date = Column(Date)
    bill_generated_date = Column(Date)
    is_bill_generated = Column(Boolean, default=False)
    is_payment_completed = Column(Boolean, default=False)
    credit_card_id = Column(Integer, ForeignKey("credit_cards.id", ondelete="CASCADE"))
    credit_card = relationship('CreditCard', back_populates='credit_bills')


class CreditCardPaymentDetails(Base):
    __tablename__ = "credit_payment_details"
    id = Column(Integer, primary_key=True, index=True)
    payment_amount = Column(Integer)
    payment_date = Column(DateTime, default=func.now())
    credit_card_id = Column(Integer, ForeignKey("credit_cards.id", ondelete="CASCADE"))
    credit_card = relationship('CreditCard', back_populates='creditcard_payments')

