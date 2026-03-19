from dotenv import load_dotenv
from os import getenv
load_dotenv()

class Config():
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"