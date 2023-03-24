from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String

from app.database.base import Base
from app.database.mixins import TimestampMixin

class UserProfileModel(Base, TimestampMixin):
    __tablename__ = "user_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)