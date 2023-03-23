import re
from typing import Dict, Optional
from pydantic import BaseModel, validator
from pydantic import PydanticValueError

class LoginSchema(BaseModel):
    email: Optional[str]
    password: Optional[str]
    
    @validator("email", always=True)
    def validate_email(cls, value: str, values: Dict, **kwargs) -> str:
        if not value:
            raise PydanticValueError(msg_template="email is requiered")
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(regex, value):
            raise PydanticValueError(msg_template="invalid email")
        return value
    
    @validator("password", always=True)
    def validate_password(cls, value: str, values: Dict, **kwargs) -> str:
        if not value:
            raise PydanticValueError(msg_template="password is required")
        return value