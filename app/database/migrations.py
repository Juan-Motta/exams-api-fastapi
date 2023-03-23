from app.models.user import UserModel

from app.database.base import Base, engine

def create_tables() -> None:
    Base.metadata.create_all(engine)