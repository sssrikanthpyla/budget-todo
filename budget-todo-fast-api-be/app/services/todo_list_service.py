from sqlalchemy.orm import Session, selectinload
from app.models.todo_list import Todo, SubTask
from app.schemas.todo_list_schema import TodoCreate, TodoUpdate

def get_todo_list(db: Session, id: int, user_id: int):
    return db.query(Todo).options(selectinload(Todo.sub_tasks)).filter(Todo.id == id, Todo.user_id == user_id).first()

def get_todo_lists(db: Session, user_id: int):
    return db.query(Todo).options(selectinload(Todo.sub_tasks)).filter(Todo.user_id == user_id).all()

def create_todo_list(db: Session, todoList: TodoCreate, user_id):
    db_todo = Todo(
        title=todoList.title,
        description=todoList.description,
        due_date=todoList.due_date,
        is_dependency=todoList.is_dependency,
        is_completed=todoList.is_completed,
        user_id=user_id
    )
    for subtask in todoList.sub_tasks:
        db_subtask = SubTask(**subtask.model_dump(), todo=db_todo)
        db.add(db_subtask)
    
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo_list(db: Session, db_todo_list: Todo, todoList: TodoUpdate):
    db_todo_list.title=todoList.title,
    db_todo_list.description=todoList.description,
    db_todo_list.due_date=todoList.due_date,
    db_todo_list.is_dependency=todoList.is_dependency
    db_todo_list.is_completed=todoList.is_completed
    
    if todoList.sub_tasks:
        existing_subtask_ids = [subtask.id for subtask in db_todo_list.sub_tasks]
        for update_subtask in todoList.sub_tasks:
            if update_subtask.id:
                existing_subtask_ids.remove(update_subtask.id)
        for subtask_id in existing_subtask_ids:
            db.query(SubTask).filter(SubTask.id == subtask_id).delete()
        
        for subtask_data in todoList.sub_tasks:
            subtask = db.query(SubTask).filter(SubTask.id == subtask_data.id).first()
            if subtask:
                subtask.title = subtask_data.title
                subtask.description = subtask_data.description
                subtask.due_date = subtask_data.due_date
                subtask.is_completed = subtask_data.is_completed
            else:
                new_subtask = SubTask(**subtask_data.model_dump(), todo=db_todo_list)
                db.add(new_subtask)
    
    db.commit()
    db.refresh(db_todo_list)
    return db_todo_list

def delete_todo_list(db: Session, db_todo_list: Todo):
    db.delete(db_todo_list)
    db.commit()
    return {"status": "Success", "message": "Todo list deleted successfully"}
