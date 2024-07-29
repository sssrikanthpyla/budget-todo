from sqlalchemy.orm import Session
from app.models.key_notes import Keynotes
from app.schemas.key_notes_schema import KeynotesCreate, KeynotesUpdate

def get_key_notes(db: Session, id: int, user_id: int):
    return db.query(Keynotes).filter(Keynotes.id == id, Keynotes.user_id == user_id).first()

def get_all_key_notes(db: Session, user_id: int):
    return db.query(Keynotes).filter(Keynotes.user_id == user_id).all()

def create_key_note(db: Session, keynote: KeynotesCreate, user_id):
    db_key_note = Keynotes(
        name=keynote.name,
        purpose=keynote.purpose,
        description=keynote.description,
        star=keynote.star,
        user_id=user_id
    )
    db.add(db_key_note)
    db.commit()
    db.refresh(db_key_note)
    return db_key_note

def update_key_note(db: Session, db_key_note: Keynotes, keynote: KeynotesUpdate):
    db_key_note.name=keynote.name,
    db_key_note.purpose=keynote.purpose,
    db_key_note.description=keynote.description,
    db_key_note.star=keynote.star
    db.commit()
    db.refresh(db_key_note)
    return db_key_note

def delete_key_note(db: Session, db_key_note: Keynotes):
    db.delete(db_key_note)
    db.commit()
    return {"status": "Success", "message": "Keynote deleted successfully"}
