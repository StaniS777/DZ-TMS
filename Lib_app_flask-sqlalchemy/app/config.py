import os

from dotenv import load_dotenv
load_dotenv()


class Config:
    FLASK_DEBUG: bool = bool(os.getenv("FLASK_DEBUG")) 
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URI")
