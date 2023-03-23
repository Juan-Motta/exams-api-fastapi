from datetime import datetime

from fastapi import Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from app.schemas.login import LoginSchema
from app.database.sessions import get_db
from app.services.login import get_user_service
from app.models.user import UserModel
from app.config.error_handler import ApiError

def login_controller(request: LoginSchema, db: Session = Depends(get_db)) -> JSONResponse:
    user: UserModel = get_user_service(db, request)
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "active": user.active
    }
