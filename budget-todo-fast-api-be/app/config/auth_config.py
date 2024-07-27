import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()

class AuthSettings(BaseSettings):
    DOMAIN: str
    API_AUDIENCE: str
    ISSUER: str
    ALGORITHMS: str
    
    class AuthConfig:
        env_file = ".env"

authSettings = AuthSettings()