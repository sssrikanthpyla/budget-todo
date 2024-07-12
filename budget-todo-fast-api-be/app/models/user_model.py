from pydantic import BaseModel

# Pydantic model for User
class User(BaseModel):
    username: str
    email: str