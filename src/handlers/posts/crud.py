from sqlalchemy.ext.asyncio import AsyncSession, async_session
from sqlalchemy import select
from database_config import engine
from src.models import Post


async def get_posts():
    """Получние списка постов"""
    async with AsyncSession(bind=engine) as session:
        res = await session.execute(select(Post))
        posts = res.scalars().all()
        return posts