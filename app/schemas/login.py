import re
from typing import Dict, Optional
from pydantic import BaseModel, validator

from app.config.error_handler import ValidationError

class LoginSchema(BaseModel):
    email: Optional[str]
    password: Optional[str]
    
    @validator("email", always=True)
    def validate_email(cls, value: str, values: Dict, **kwargs) -> str:
        if not value:
            raise ValidationError(email="email is requiered")
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(regex, value):
            raise ValidationError(email="invalid email")
        return value
    
    @validator("password", always=True)
    def validate_password(cls, value: str, values: Dict, **kwargs) -> str:
        if not value:
            raise ValidationError(password="password is required")
        return value