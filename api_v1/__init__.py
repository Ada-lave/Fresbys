from fastapi import APIRouter
from .users.routers import router as user_router
from .group.routers import router as group_router

router = APIRouter()

router.include_router(user_router, tags=["Users"])
router.include_router(group_router, tags=["Groups"])
