from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import card_service
from app.models import card_model
from app.schemas import card_schema
from app.database.database_configure import get_db

router = APIRouter()

@router.post("/cards", response_model=card_schema.Card)
async def save_cards(card: card_schema.CardCreate, db: Session=Depends(get_db)):
    return card_service.create_card(db=db, card=card)

@router.get("/cards", response_model=list[card_schema.Card])
async def get_all_cards(db: Session = Depends(get_db)):
    return card_service.get_all_card_details(db=db)

@router.get("/cards/{id}", response_model=card_schema.Card)
async def get_card(id: int, db: Session = Depends(get_db)):
    db_card = card_service.get_card_details(db=db, id=id)
    if db_card is None:
        raise HTTPException(status_code=404, details="Card not found")
    return db_card

@router.put("/cards/{id}", response_model=card_schema.Card)
async def update_card(id: int, card: card_schema.CardUpdate, db: Session = Depends(get_db)):
    db_card = card_service.get_card_details(db=db, id=id)
    if db_card is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return card_service.update_card(db=db, db_card=db_card, card=card)

@router.delete("/items/{id}")
async def delete_card(id: int, db: Session = Depends(get_db)):
    db_card = card_service.get_card_details(db=db, id=id)
    if db_card is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return card_service.delete_card(db=db, db_card=db_card)