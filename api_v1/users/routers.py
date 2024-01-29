from fastapi import APIRouter, Depends
from core.config.db_helper import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import UserBase, CreateUser, User
from .crud import get_all, add_user, get_user_with_group_by_id

router = APIRouter(prefix="/users")


@router.get("")
async def get_all_users(
    session: AsyncSession = Depends(db_helper.session_depends),
) -> list[User]:
    user = await get_all(session=session)

    return user


@router.get("/{user_id}/")
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(db_helper.session_depends),
):
    user = await get_user_with_group_by_id(session=session, user_id=user_id)
    
    return user


@router.post("")
async def create_user(
    user: CreateUser,
    session: AsyncSession = Depends(db_helper.session_depends),
) -> User:
    return await add_user(session=session, user=user)
