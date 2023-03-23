from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = f"""postgresql://{DB["user"]}:{DB["password"]}@{DB["host"]}:{DB["port"]}/{DB["name"]}"""
DATABASE_URL = f"""sqlite:///./db.db"""

engine: Engine = create_engine(DATABASE_URL)

Session: sessionmaker = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()

