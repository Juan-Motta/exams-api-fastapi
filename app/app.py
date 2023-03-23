from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.routers.base import router as base_router
from app.routers.user import router as users_router
from app.database.migrations import create_tables
from app.config.error_handler import ApiError


app: FastAPI = FastAPI()

app.include_router(base_router)
app.include_router(users_router)

@app.on_event("startup")
async def startup_event() -> None:
    create_tables()

@app.on_event("shutdown")
async def shutdown() -> None:
    pass

@app.exception_handler(ApiError)
async def custom_error_handler(request: Request, exc: ApiError):
    return JSONResponse(
        status_code=exc.code,
        content={
            "code": exc.code,
            "success": False,
            "message": str(exc),
            "time_stamp": datetime.now().strftime("%y-%m-%d %H:%M:%S")
        },
    )
    
@app.exception_handler(RequestValidationError)
async def custom_error_handler(request: Request, exc: RequestValidationError):
    print(exc.errors())
    errors = [error.get("ctx") for error in exc.errors()]
    return JSONResponse(
        status_code=400,
        content={
            "code": 400,
            "success": False,
            "errors": errors,
            "time_stamp": datetime.now().strftime("%y-%m-%d %H:%M:%S")
        },
    )