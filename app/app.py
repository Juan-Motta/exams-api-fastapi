from fastapi import FastAPI

from app.routers.base import router as base_router
from app.routers.user import router as users_router

from app.database.migrations import create_tables

app: FastAPI = FastAPI()

app.include_router(base_router)
app.include_router(users_router)

@app.on_event("startup")
async def startup_event() -> None:
    create_tables()

@app.on_event("shutdown")
async def shutdown() -> None:
    pass