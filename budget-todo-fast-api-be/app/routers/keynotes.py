from typing import List
from fastapi import Response, APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.services import key_notes_service
from app.schemas import key_notes_schema
from app.utils.utils import VerifyToken
from app.config.database_configure import get_db

router = APIRouter(prefix="/keynote")

token_auth_scheme = HTTPBearer()

@router.post("/note", response_model=key_notes_schema.Keynotes, description="Create a new Keynote")
async def save_key_note(
    response: Response, 
    keynote: key_notes_schema.KeynotesCreate, 
    db: Session=Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return key_notes_service.create_key_note(db=db, keynote=keynote, user_id=result['user'].id)

@router.get("/notes", response_model=List[key_notes_schema.Keynotes], description="Fetch all Keynote details")
async def get_all_keynotes(
    response: Response, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return key_notes_service.get_all_key_notes(db=db, user_id=result['user'].id)

@router.get("/note/{id}", response_model=key_notes_schema.Keynotes, description="Fetch Keynote details based on id")
async def get_keynote(
    response: Response, 
    id: int, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    db_key_note = key_notes_service.get_key_notes(db=db, id=id, user_id=result['user'].id)
    if db_key_note is None:
        raise HTTPException(status_code=404, details="Card not found")
    return db_key_note

@router.put("/note/{id}", response_model=key_notes_schema.Keynotes, description="Update Keynote details based on id")
async def update_keynote(
    response: Response, 
    id: int, 
    keynote: key_notes_schema.KeynotesUpdate, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    db_key_note = key_notes_service.get_key_notes(db=db, id=id, user_id=result['user'].id)
    if db_key_note is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return key_notes_service.update_key_note(db=db, db_key_note=db_key_note, keynote=keynote)

@router.delete("/note/{id}", description="Delete Keynote details based on id")
async def delete_keynote(
    response: Response, 
    id: int, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    db_key_note = key_notes_service.get_key_notes(db=db, id=id, user_id=result['user'].id)
    if db_key_note is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return key_notes_service.delete_key_note(db=db, db_key_note=db_key_note)