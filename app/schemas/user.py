import re
from typing import Dict, Optional
from pydantic import BaseModel, validator, root_validator, PydanticValueError

class UserSchema(BaseModel):
    id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    password_confirmation: Optional[str]
    
    @validator("first_name", "last_name", always=True)
    def validate_name(cls, value: str, values: Dict, **kwargs) -> str:
        field: str = kwargs["field"].name.replace("_", " ")
        if not value:
            raise PydanticValueError(msg_template=f"{field} is required")
        pattern = r"(?:.*[\d\W_].*)"
        if re.fullmatch(pattern, value):
            raise PydanticValueError(msg_template=f"invalid {field}")
        return value
    
    @validator("email", always=True)
    def validate_email(cls, value: str, values: Dict, **kwargs) -> str:
        if not value:
            raise PydanticValueError(msg_template="email is required")
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(pattern, value):
            raise PydanticValueError(msg_template="invalid email")
        return value
    
    @validator("password", "password_confirmation", always=True)
    def validate_password(cls, value: str, values: Dict, **kwargs) -> str:
        if not value:
            raise PydanticValueError(msg_template="password is required")
        return value
    
    @root_validator
    def validate_passwords_match(cls, values: Dict) -> Dict:
        pw1 = values.get("password") 
        pw2 = values.get("password_confirmation")
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise PydanticValueError(msg_template="passwords do not match")
        return values