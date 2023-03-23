from fastapi import Depends, Response

from sqlalchemy.orm import Session

from app.schemas.user import UserSchema
from app.database.sessions import get_db
from app.services.user import create_user_service

def create_user_controller(request: UserSchema, db: Session = Depends(get_db)) -> Response:
    return create_user_service(db, request)