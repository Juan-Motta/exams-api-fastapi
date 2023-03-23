from pydantic import PydanticValueError

class ApiError(ValueError):
    code: int = 400
    
    def __init__(self, message: str, code: int = 400):
        super().__init__(message)
        self.code = code
        

class ValidationError(PydanticValueError):
    msg_template = "Validation error"
    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)