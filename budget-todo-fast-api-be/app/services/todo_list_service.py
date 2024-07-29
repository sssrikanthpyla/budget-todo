from sqlalchemy.orm import Session
from app.models.todo_list import TodoList
from app.schemas.todo_list_schema import TodoListCreate, TodoListUpdate

def get_todo_list(db: Session, id: int, user_id: int):
    return db.query(TodoList).filter(TodoList.id == id, TodoList.user_id == user_id).first()

def get_todo_lists(db: Session, user_id: int):
    return db.query(TodoList).filter(TodoList.user_id == user_id).all()

def create_todo_list(db: Session, todoList: TodoListCreate, user_id):
    db_key_note = TodoList(
        name=todoList.name,
        purpose=todoList.purpose,
        description=todoList.description,
        priority=todoList.priority,
        user_id=user_id
    )
    db.add(db_key_note)
    db.commit()
    db.refresh(db_key_note)
    return db_key_note

def update_todo_list(db: Session, db_todo_list: TodoList, todoList: TodoListUpdate):
    db_todo_list.name=todoList.name,
    db_todo_list.purpose=todoList.purpose,
    db_todo_list.description=todoList.description,
    db_todo_list.priority=todoList.priority
    db.commit()
    db.refresh(db_todo_list)
    return db_todo_list

def delete_todo_list(db: Session, db_todo_list: TodoList):
    db.delete(db_todo_list)
    db.commit()
    return {"status": "Success", "message": "Todo list deleted successfully"}
