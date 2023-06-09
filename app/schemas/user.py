import re
from typing import Dict, Optional
from pydantic import BaseModel, validator, root_validator, PydanticValueError

from app.config.error_handler import ValidationError
from app.utils.password_hash import hash_password


class UserCreateSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    password_confirmation: Optional[str]
    
    @validator("first_name", "last_name", always=True)
    def validate_name(cls, value: str, values: Dict, **kwargs) -> str:
        field_name: str = kwargs["field"]
        field: str = kwargs["field"].name.replace("_", " ")
        if not value:
            raise ValidationError({field_name:f"{field} is required"})
        pattern = r"(?:.*[\d\W_].*)"
        if re.fullmatch(pattern, value):
            raise ValidationError({field_name:f"invalid {field}"})
        return value
    
    @validator("email", always=True)
    def validate_email(cls, value: str, values: Dict, **kwargs) -> str:
        if not value:
            raise ValidationError(email="email is required")
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(pattern, value):
            raise ValidationError(email="invalid email")
        return value
    
    @validator("password", "password_confirmation", always=True)
    def validate_password(cls, value: str, values: Dict, **kwargs) -> str:
        if not value:
            raise ValidationError(password="password is required")
        return value
    
    @root_validator
    def validate_passwords_match(cls, values: Dict) -> Dict:
        pw1: Optional[str] = values.get("password") 
        pw2: Optional[str] = values.get("password_confirmation")
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValidationError(password="passwords do not match")
        hashed_password: str = hash_password(pw1)
        values["password"] = hashed_password
        values["password_confirmation"] = hashed_password
        return values
    

class UserUpdateSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    password_confirmation: Optional[str]
    
    @validator("first_name", "last_name", always=True)
    def validate_name(cls, value: str, values: Dict, **kwargs) -> str:
        field_name: str = kwargs["field"]
        field: str = kwargs["field"].name.replace("_", " ")
        if not value:
            return value
        pattern = r"(?:.*[\d\W_].*)"
        if re.fullmatch(pattern, value):
            raise ValidationError({field_name:f"invalid {field}"})
        return value
    
    @validator("email", always=True)
    def validate_email(cls, value: str, values: Dict, **kwargs) -> str:
        if not value:
            return value
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(pattern, value):
            raise ValidationError(email="invalid email")
        return value
    
    @validator("password", "password_confirmation", always=True)
    def validate_password(cls, value: str, values: Dict, **kwargs) -> str:
        if not value:
            return value
        return value
    
    @root_validator
    def validate_passwords_match(cls, values: Dict) -> Dict:
        pw1: Optional[str] = values.get("password") 
        pw2: Optional[str] = values.get("password_confirmation")
        if pw1 is None or pw2 is None:
            return values
        if pw1 != pw2:
            raise ValidationError(password="passwords do not match")
        hashed_password: str = hash_password(pw1)
        values["password"] = hashed_password
        values["password_confirmation"] = hashed_password
        return values


class UserBaseSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    active: bool

    class Config:
        orm_mode = True