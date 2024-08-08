from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime


# Credit card Transactions Schema
class CreditTransactionBase(BaseModel):
    amount: float
    transaction_date: datetime
    description: str

class CreditTransactionCreate(CreditTransactionBase):
    credit_card_id: int

class CreditTransactionUpdate(CreditTransactionBase):
    pass

class CreditTransaction(CreditTransactionBase):
    id: int
    
    class Config:
        from_attributes = True


# Credit card Bills Schema
class CreditBillsBase(BaseModel):
    bill_due_date: date
    bill_generated_date: date
    is_bill_generated: bool
    is_payment_completed: bool

class CreditBillsCreate(CreditBillsBase):
    credit_card_id: int

class CreditBillsUpdate(CreditBillsBase):
    pass

class CreditBills(CreditBillsBase):
    id: int
    
    class Config:
        from_attributes = True


# Credit card Payment Details Schema
class CreditCardPaymentDetailsBase(BaseModel):
    bill_due_date: date
    bill_generated_date: date
    is_bill_generated: bool
    is_payment_completed: bool

class CreditCardPaymentDetailsCreate(CreditCardPaymentDetailsBase):
    credit_card_id: int

class CreditCardPaymentDetailsUpdate(CreditCardPaymentDetailsBase):
    pass

class CreditCardPaymentDetails(CreditCardPaymentDetailsBase):
    id: int
    
    class Config:
        from_attributes = True


# Credit card Schema
class CreditCardBase(BaseModel):
    card_number: str
    card_type: str
    card_name: str
    card_issued_by: str
    cardholder_name: str
    expiry_date: date
    cvv: int

class CreditCardCreate(CreditCardBase):
    user_id: int
    credit_transactions: List[CreditTransactionCreate] = []
    credit_bills: List[CreditBillsCreate] = []
    creditcard_payments: List[CreditCardPaymentDetailsCreate] = []

class CreditCardUpdate(CreditCardBase):
    credit_transactions: Optional[List[CreditTransactionCreate]] = None
    credit_bills: Optional[List[CreditBillsCreate]] = None
    creditcard_payments: Optional[List[CreditCardPaymentDetailsCreate]] = None

class CreditCard(CreditCardBase):
    id: int
    credit_transactions: List[CreditTransaction] = []
    credit_bills: List[CreditBills] = []
    creditcard_payments: List[CreditCardPaymentDetails] = []
    
    class Config:
        from_attributes = True