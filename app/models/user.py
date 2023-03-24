from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String

from app.database.base import Base
from app.database.mixins import TimestampMixin

class UserModel(Base, TimestampMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False, unique=True)
    password = Column(String, nullable=False, index=True)
    