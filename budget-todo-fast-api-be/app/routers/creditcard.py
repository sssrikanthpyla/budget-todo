from fastapi import Response, APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.services import creditcard_service
from app.schemas.creditcard_schema import CreditCard, CreditCardCreate, CreditCardUpdate
from app.utils.utils import VerifyToken
from app.config.database_configure import get_db

router = APIRouter(prefix="/creditcard")

token_auth_scheme = HTTPBearer()

@router.post("/cards", response_model=CreditCard, description="Create a new credit card")
async def save_cards(
    response: Response, 
    card: CreditCardCreate, 
    db: Session=Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return creditcard_service.create_card(db=db, card=card, user_id=result['user'].id)

@router.get("/cards", response_model=list[CreditCard], description="Fetch all credit card details")
async def get_all_cards(
    response: Response, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return creditcard_service.get_all_card_details(db=db, user_id=result['user'].id)

@router.get("/cards/{id}", response_model=CreditCard, description="Fetch credit card details based on id")
async def get_card(
    response: Response, 
    id: int, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    db_card = creditcard_service.get_card_details(db=db, id=id, user_id=result['user'].id)
    if db_card is None:
        raise HTTPException(status_code=404, details="Card not found")
    return db_card

@router.put("/cards/{id}", response_model=CreditCard, description="Update credit card details based on id")
async def update_card(
    response: Response, 
    id: int, 
    card: CreditCardUpdate, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    db_card = creditcard_service.get_card_details(db=db, id=id, user_id=result['user'].id)
    if db_card is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return creditcard_service.update_card(db=db, db_card=db_card, card=card)

@router.delete("/cards/{id}", description="Delete credit card details based on id")
async def delete_card(
    response: Response, 
    id: int, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    db_card = creditcard_service.get_card_details(db=db, id=id, user_id=result['user'].id)
    if db_card is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return creditcard_service.delete_card(db=db, db_card=db_card)