from fastapi import Response, APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.services import user_servce
from app.utils.utils import VerifyToken
from app.config.database_configure import get_db

router = APIRouter(prefix="/user")

token_auth_scheme = HTTPBearer()

@router.delete("/delete_account", description="Delete account permanently")
async def delete_user(response: Response, db: Session = Depends(get_db), token: str = Depends(token_auth_scheme)):
    result = VerifyToken(token.credentials).get_current_user(db=db)
    if result['status'] == 'Failed':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    db_user = user_servce.get_user(db=db, email=result['user'].email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return user_servce.delete_user(db=db, db_user=db_user)