from sqlalchemy.ext.asyncio import AsyncSession, async_session
from sqlalchemy import select
from database_config import engine
from src.models import Post, AdditionalPost


async def get_posts():
    """Получние списка постов"""
    async with AsyncSession(bind=engine) as session:
        res = await session.execute(select(Post))
        posts = res.scalars().all()
        return posts


async def get_post(post_id: int):
    """Получени поста по id"""
    async with AsyncSession(bind=engine) as session:
        res = await session.execute(select(Post).where(Post.id == post_id))
        return res.scalars().first()


async def get_additional_posts():
    """Получние списка доп. постов"""
    async with AsyncSession(bind=engine) as session:
        res = await session.execute(select(AdditionalPost))
        posts = res.scalars().all()
        return posts


async def get_additional_post(post_id: int):
    """Получени поста по id"""
    async with AsyncSession(bind=engine) as session:
        res = await session.execute(select(AdditionalPost).where(AdditionalPost.id == post_id))
        return res.scalars().first()