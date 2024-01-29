from core.config.db_helper import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from core.models.group import Group
from core.models.user import User
from .schemas import CreateGroup, Group as SGroup


async def get_all(session: AsyncSession) -> list[SGroup]:
    stmt = select(Group).order_by(Group.name)
    groups = await session.scalars(stmt)

    return list(groups)


async def add_group(
    session: AsyncSession,
    group: CreateGroup,
) -> SGroup:
    group = Group(**group.model_dump())
    session.add(group)
    await session.commit()
    return group

async def get_group_with_users(session: AsyncSession, group_id: int):
    stmt = select(Group).options(joinedload(Group.users)).where(Group.id == group_id)
    
    group = await session.scalar(stmt)
    
    return group
    
