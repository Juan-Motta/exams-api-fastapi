from fastapi import APIRouter

from app.controllers.app import app_base_controller

router: APIRouter = APIRouter(
    prefix="/v1"
)

router.get("")(app_base_controller)