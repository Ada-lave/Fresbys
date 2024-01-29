from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from asyncio import current_task
from core.config.conf import settings


class DatabaseHelper:
    def __init__(self):
        self.engine = create_async_engine(url=settings.db_settings.url)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_current_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        
        return session
    
    async def session_depends(self) -> AsyncSession:
        session = self.get_current_session()
        
        async with session() as sess:
            yield sess
            await session.remove()


db_helper: DatabaseHelper = DatabaseHelper()