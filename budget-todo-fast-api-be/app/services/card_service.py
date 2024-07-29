from sqlalchemy.orm import Session
from app.models.card_model import Card
from app.schemas.card_schema import CardCreate, CardUpdate

def get_card_details(db: Session, id: int, user_id: int):
    return db.query(Card).filter(Card.id == id, Card.user_id == user_id).first()

def get_all_card_details(db: Session, user_id: int):
    return db.query(Card).filter(Card.user_id == user_id).all()

def create_card(db: Session, card: CardCreate, user_id):
    db_card = Card(
        card_number=card.card_number,
        name_of_card=card.name_of_card,
        card_title=card.card_title,
        bill_generation_date=card.bill_generation_date,
        payment_due_date=card.payment_due_date,
        payment_completed_date=card.payment_completed_date,
        is_payment_completed=card.is_payment_completed,
        is_bill_generated=card.is_bill_generated,
        user_id=user_id
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

def update_card(db: Session, db_card: Card, card: CardUpdate):
    db_card.card_number=card.card_number,
    db_card.name_of_card=card.name_of_card,
    db_card.card_title=card.card_title,
    db_card.bill_generation_date=card.bill_generation_date,
    db_card.payment_due_date=card.payment_due_date,
    db_card.payment_completed_date=card.payment_completed_date,
    db_card.is_payment_completed=card.is_payment_completed,
    db_card.is_bill_generated=card.is_bill_generated
    db.commit()
    db.refresh(db_card)
    return db_card

def delete_card(db: Session, db_card: Card):
    db.delete(db_card)
    db.commit()
    return {"message": "Card deleted successfully"}
