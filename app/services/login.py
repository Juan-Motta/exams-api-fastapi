from typing import Dict
from sqlalchemy.orm.session import Session

from app.schemas.login import LoginSchema
from app.models.user import UserModel
from app.utils.password_hash import verify_password
from app.config.error_handler import ApiError

def get_user_service(db: Session, request: LoginSchema) -> Dict:
    user: UserModel = db.query(UserModel).filter(UserModel.email == request.email).first()
    if not user:
        raise ApiError("invalid authetication data")
    is_password_correct = verify_password(user.password, request.password)
    if not is_password_correct:
        raise ApiError("invalid authetication data")
    return user