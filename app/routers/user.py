from fastapi import APIRouter

from app.controllers.user import (
    create_user_controller, 
    update_user_controller, 
    delete_user_controller,
    retrieve_all_user_controller,
    retrieve_one_user_controller
)

router: APIRouter = APIRouter(
    prefix="/v1/users",
    tags=["users"]
)

router.get("")(retrieve_all_user_controller)
router.post("")(create_user_controller)
router.get("/{user_id}")(retrieve_one_user_controller)
router.patch("/{user_id}")(update_user_controller)
router.delete("/{user_id}")(delete_user_controller)

