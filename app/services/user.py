from typing import Dict
from sqlalchemy.orm.session import Session

from app.schemas.user import UserSchema
from app.models.user import UserModel

def create_user_service(db: Session, request: UserSchema) -> Dict:
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