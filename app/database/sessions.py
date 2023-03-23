from app.database.base import Base, Session, engine

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
        
def create_tables() -> None:
    Base.metadata.create_all(engine)