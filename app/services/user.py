from typing import Dict
from sqlalchemy.orm.session import Session

from app.schemas.user import UserCreateSchema, UserUpdateSchema
from app.models.user import UserModel
from app.config.error_handler import ApiError

def create_user_service(db: Session, request: UserCreateSchema) -> Dict:
    user: UserModel = UserModel(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=request.password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user_service(db: Session, request: UserUpdateSchema, id: int) -> Dict:
    user: UserModel = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise ApiError("invalid authetication data")
    if request.first_name:
        user.first_name = request.first_name
    if request.last_name:
        user.last_name = request.last_name
    if request. email:
        user.email = request.email
    if request.password:
        user.password = request.password
    return user
    