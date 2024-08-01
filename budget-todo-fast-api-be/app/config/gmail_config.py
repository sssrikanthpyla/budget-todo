import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()

class GmailSettings(BaseSettings):
    G_PWD: str
    G_USER: str
    
    class AuthConfig:
        env_file = ".env"

gmailSettings = GmailSettings()