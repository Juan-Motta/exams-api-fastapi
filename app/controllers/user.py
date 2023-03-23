from fastapi import Depends, Response

from sqlalchemy.orm import Session

from app.schemas.user import UserSchema
from app.database.sessions import get_db
from app.services.user import create_user_service
from app.models.user import UserModel

def create_user_controller(request: UserSchema, db: Session = Depends(get_db)) -> Response:
    user: UserModel = create_user_service(db, request)
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "active": user.active
    }