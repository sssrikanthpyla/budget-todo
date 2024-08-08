from typing import List
from fastapi import Response, APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.services import todo_list_service
from app.schemas import todo_list_schema
from app.utils.utils import VerifyToken
from app.config.database_configure import get_db

router = APIRouter(prefix="/todo")

token_auth_scheme = HTTPBearer()

@router.post("/list", response_model = todo_list_schema.Todo, description="Create a new Todo List")
async def save_todo_list(
    response: Response, 
    todoList: todo_list_schema.TodoCreate, 
    db: Session=Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return todo_list_service.create_todo_list(db=db, todoList=todoList, user_id=result['user'].id)

@router.get("/lists", response_model=List[todo_list_schema.Todo], description="Fetch all Todo List details")
async def get_all_todo_lists(
    response: Response, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return todo_list_service.get_todo_lists(db=db, user_id=result['user'].id)

@router.get("/list/{id}", response_model=todo_list_schema.Todo, description="Fetch Todo List details based on id")
async def get_todo(
    response: Response, 
    id: int, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    db_todo = todo_list_service.get_todo_list(db=db, id=id, user_id=result['user'].id)
    if db_todo is None:
        raise HTTPException(status_code=404, details="Card not found")
    return db_todo

@router.put("/list/{id}", response_model=todo_list_schema.Todo, description="Update Todo List details based on id")
async def update_todo(
    response: Response, 
    id: int, 
    todoList: todo_list_schema.TodoUpdate, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    db_todo = todo_list_service.get_todo_list(db=db, id=id, user_id=result['user'].id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return todo_list_service.update_todo_list(db=db, db_todo_list=db_todo, todoList=todoList)

@router.delete("/list/{id}", description="Delete Todo List details based on id")
async def delete_todo(
    response: Response, 
    id: int, 
    db: Session = Depends(get_db), 
    token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    db_todo = todo_list_service.get_todo_list(db=db, id=id, user_id=result['user'].id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return todo_list_service.delete_todo_list(db=db, db_todo_list=db_todo)