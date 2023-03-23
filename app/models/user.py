from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean

from app.database.base import Base

class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, onupdate=datetime.now)
    active = Column(Boolean, default=True)
    