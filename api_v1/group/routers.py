from fastapi import APIRouter, Depends
from core.config.db_helper import db_helper
from .crud import add_group, get_all, get_group_with_users
from .schemas import Group, CreateGroup
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix="/groups")


@router.get("/")
async def all_groups(
    session: AsyncSession = Depends(db_helper.session_depends),
) -> list[Group]:
    groups = await get_all(session=session)
    return groups


@router.get("/{group_id}/")
async def group_with_users_by_id(
    group_id: int,
    session: AsyncSession = Depends(db_helper.session_depends),
):
    groups = await get_group_with_users(session=session, group_id=group_id)
    
    return groups


@router.post("/")
async def create_group(
    group: CreateGroup,
    session: AsyncSession = Depends(db_helper.session_depends),
) -> Group:
    group = await add_group(session=session, group=group)

    return group
