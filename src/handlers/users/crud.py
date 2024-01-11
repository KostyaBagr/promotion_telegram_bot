from sqlalchemy.ext.asyncio import AsyncSession, async_session
from sqlalchemy import select

from database_config import engine
from src.models import User


async def create_user(data: dict):
    """Function to create a user"""
    async with AsyncSession(bind=engine) as session:
        db_user = User(name=data['name'], username=data['username'], telegram_id=data['telegram_id'])
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user


async def is_user(telegram_id: int):
    """Функция проверят существует ли юзер"""
    async with AsyncSession(bind=engine) as session:
        res = await session.execute(select(User).where(User.telegram_id == telegram_id))
        return res.scalars().first()
