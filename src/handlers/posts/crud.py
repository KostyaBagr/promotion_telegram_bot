from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database_config import engine
from src.models import Post, AdditionalPost
from typing import Union
from sqlalchemy import delete

async def get_posts(model: Union[Post, AdditionalPost]):
    """Получние списка постов"""
    async with AsyncSession(bind=engine) as session:
        res = await session.execute(select(model))
        posts = res.scalars().all()
        return posts


async def get_post(post_id: int, model: Union[Post, AdditionalPost]):
    """Получени поста по id"""
    async with AsyncSession(bind=engine) as session:
        res = await session.execute(select(model).where(model.id == post_id))
        return res.scalars().first()


async def delete_post(post_id: int, model: Union[Post, AdditionalPost]):
    """Удаление поста по id"""
    async with AsyncSession(bind=engine) as session:

        res = await session.execute(select(model).where(model.id == post_id))
        res = res.scalar_one()
        await session.delete(res)
        await session.commit()
        return res