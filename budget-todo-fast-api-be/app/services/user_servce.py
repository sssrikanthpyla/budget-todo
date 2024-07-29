from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        username=user.username,
        nickname=user.nickname
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_with_payload(db: Session, user: UserCreate):
    db_user = User(
        email=user['email'],
        username=user['name'],
        nickname=user['nickname']
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: User):
    db.delete(db_user)
    db.commit()
    return {"status": "Success", "message": "User deleted successfully"}