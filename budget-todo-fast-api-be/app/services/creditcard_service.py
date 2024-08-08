from sqlalchemy.orm import Session
from app.models.creditcard_model import CreditCard, CreditTransaction, CreditCardPaymentDetails, Bill
from app.schemas.creditcard_schema import CreditCardCreate, CreditCardUpdate

def get_card_details(db: Session, id: int, user_id: int):
    return db.query(CreditCard).filter(CreditCard.id == id, CreditCard.user_id == user_id).first()

def get_all_card_details(db: Session, user_id: int):
    return db.query(CreditCard).filter(CreditCard.user_id == user_id).all()

def create_card(db: Session, card: CreditCardCreate, user_id):
    db_card = CreditCard(
        card_number=card.card_number,
        card_type=card.card_type,
        card_name=card.card_name,
        card_issued_by=card.card_issued_by,
        cardholder_name=card.cardholder_name,
        expiry_date=card.expiry_date,
        cvv=card.cvv,
        user_id=user_id
    )
    
    for transaction in card.credit_transactions:
        db_transaction = CreditTransaction(**transaction.model_dump(), credit_card=db_card)
        db.add(db_transaction)
    
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

def update_card(db: Session, db_card: CreditCard, card: CreditCardUpdate):
    db_card.card_number=card.card_number,
    db_card.card_type=card.card_type,
    db_card.card_name=card.card_name,
    db_card.card_issued_by=card.card_issued_by,
    db_card.cardholder_name=card.cardholder_name,
    db_card.expiry_date=card.expiry_date,
    db_card.cvv=card.cvv,
    db.commit()
    db.refresh(db_card)
    return db_card

def delete_card(db: Session, db_card: CreditCard):
    db.delete(db_card)
    db.commit()
    return {"status": "Success", "message": "Card deleted successfully"}
