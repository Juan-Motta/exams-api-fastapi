from fastapi import APIRouter

from app.controllers.app import app_base_controller
from app.controllers.login import login_controller

router: APIRouter = APIRouter(
    prefix="/v1"
)

router.get("")(app_base_controller)
router.post("/login")(login_controller)
