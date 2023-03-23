from fastapi import Response, Depends

from sqlalchemy.orm import Session

from app.database.sessions import get_db

def app_base_controller(db: Session = Depends(get_db)) -> Response:
    return {
        "title": "Exams API",
        "version": "0.0.1",
    }