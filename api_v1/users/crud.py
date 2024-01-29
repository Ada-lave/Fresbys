from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from core.config.db_helper import db_helper
from core.models.user import User
from .schemas import UserBase, CreateUser, User as ModelUser


async def get_all(session: AsyncSession) -> list[ModelUser]:
    stmt = select(User).options(joinedload(User.group)).order_by(User.id)
    res = await session.scalars(stmt)

    return list(res)


async def add_user(
    session: AsyncSession,
    user: CreateUser,
) -> ModelUser:
    user = User(**user.model_dump())

    session.add(user)
    await session.commit()
    return user


async def get_user_with_group_by_id(
    session: AsyncSession,
    user_id: int,
):
    stmt = select(User).options(joinedload(User.group)).where(User.id == user_id)

    user = await session.scalar(stmt)

    return user
