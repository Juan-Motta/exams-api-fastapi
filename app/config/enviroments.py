import os
from dotenv import load_dotenv

load_dotenv()

# Config
CONFIG = {
    "secret_key": os.getenv("SECRET_KEY"),
    "debug": os.getenv("DEBUG"),
    "enviroment": os.getenv("ENVIROMENT"),
}

# Database
DB = {
    "host": os.getenv("DB_HOST"),
    "name": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT"),
}