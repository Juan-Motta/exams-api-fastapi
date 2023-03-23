from fastapi import APIRouter

from app.controllers.user import create_user_controller

router: APIRouter = APIRouter(
    prefix="/v1/users",
    tags=["users"]
)

router.post("")(create_user_controller)