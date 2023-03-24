from fastapi import Depends, Response

from sqlalchemy.orm import Session

from app.schemas.user import UserCreateSchema, UserBaseSchema, UserUpdateSchema
from app.database.sessions import get_db
from app.services.user import (
    create_user_service, 
    update_user_service, 
    delete_user_service,
    get_all_user_service,
    get_one_user_service
)
from app.models.user import UserModel

def retrieve_one_user_controller(
    user_id: int,
    db: Session = Depends(get_db)
) -> Response:
    user: UserModel = get_one_user_service(db, user_id)
    return UserBaseSchema.from_orm(user)

def retrieve_all_user_controller(
    db: Session = Depends(get_db)
) -> Response:
    user: UserModel = get_all_user_service(db)
    return [UserBaseSchema.from_orm(instance) for instance in user]

def create_user_controller(
    request: UserCreateSchema, 
    db: Session = Depends(get_db)
) -> Response:
    user: UserModel = create_user_service(db, request)
    return UserBaseSchema.from_orm(user)

def update_user_controller(
    request: UserUpdateSchema, 
    user_id: int,
    db: Session = Depends(get_db)
) -> Response:
    user: UserModel = update_user_service(db, request, user_id)
    return UserBaseSchema.from_orm(user)

def delete_user_controller(
    user_id: int,
    db: Session = Depends(get_db)
) -> Response:
    user: UserModel = delete_user_service(db, user_id)
    return UserBaseSchema.from_orm(user)