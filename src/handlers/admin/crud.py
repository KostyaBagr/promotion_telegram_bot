import os
from dotenv import load_dotenv
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing import db

from database_config import engine
from src.models import User, Post

load_dotenv()


class AdminReport:
    """Класс используется для формирования отчетности в админке"""

    def __init__(self):
        pass

    async def count_objects(self, model_name):
        """Подсчет кол-ва объектов"""
        print(model_name)
        print(type(model_name))
        async with AsyncSession(bind=engine) as session:
            return session.select(model_name).count()

    async def count_active_users(self):
        """Count the number of active users."""
        async with AsyncSession(bind=engine) as session:
            result = await session.scalar(select([func.count()]).where(User.is_active == True))
            return result


async def is_admin(user_id):
    """Ф-ция проверяет является ли юзер админом"""
    return bool(user_id == int(os.getenv("ADMIN1_ID")) or user_id == int(os.getenv("ADMIN2_ID")))


async def save_admin_post(state):
    """Ф-ция сохранет пост, который был добавлен в админке"""
    async with state.proxy() as data:
        async with AsyncSession(bind=engine) as session:
            db_post = Post(
                name=data['name'],
                text=data['text'],
                file=data['file'],
                audio=data['audio']
            )
            session.add(db_post)
            await session.commit()
            await session.refresh(db_post)
            return db_post



