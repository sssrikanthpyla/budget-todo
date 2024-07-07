from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from app import crud, models, schemas
from app.services import item_crud
from app.models import item_model
from app.schemas import item_schema
from app.database.database_configure import get_db

router = APIRouter()

@router.post("/items/", response_model=item_schema.Item)
async def create_item(item: item_schema.ItemCreate, db: Session = Depends(get_db)):
    return item_crud.create_item(db=db, item=item)

@router.get("/items/{item_id}", response_model=item_schema.Item)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/items/{item_id}", response_model=item_schema.Item)
async def update_item(item_id: int, item: item_schema.ItemUpdate, db: Session = Depends(get_db)):
    db_item = item_crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_crud.update_item(db=db, db_item=db_item, item=item)

@router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_crud.delete_item(db=db, db_item=db_item)
