from fastapi import APIRouter, Depends
from app.auth.auth import get_current_user
from app.models.user_model import User

router = APIRouter(prefix="/users")

@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
