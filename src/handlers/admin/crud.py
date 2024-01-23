import os

from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing import db
from typing import Union
from database_config import engine
from src.handlers.users.crud import get_contacts
from src.models import User, Post, AdditionalPost, ContactMe
from sqlalchemy import update
load_dotenv()


class AdminReport:
    """Класс используется для формирования отчетности в админке"""

    def __init__(self):
        pass

    async def count_objects(self, model_name):
        """Подсчет кол-ва объектов"""
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


async def save_admin_post(state: FSMContext, model: Union[Post, AdditionalPost]):
    """Ф-ция сохранет пост, который был добавлен в админке"""
    async with state.proxy() as data:
        async with AsyncSession(bind=engine) as session:
            if model == Post:
                db_post = Post(
                    name=data['name'],
                    text=data['text'],
                    file=data.get("file", None),
                    audio=data.get("audio", None)

                )
            if model == AdditionalPost:
                db_post = AdditionalPost(
                    text=data['text'],
                    file_type=data.get("file_type", None),
                    file=data.get("file", None)
                )
            session.add(db_post)
            await session.commit()
            await session.refresh(db_post)
            return db_post


async def create_contacts(text):
    """Ф-ция создает объект контактов админа"""
    async with AsyncSession(bind=engine) as session:
        contact = ContactMe(
            text=text
        )
        session.add(contact)
        await session.commit()
        await session.refresh(contact)


# async def get_contacts():
#     """Ф-ция получает контакты"""
#     async with AsyncSession(bind=engine) as session:
#         contacts = await session.execute(select(ContactMe))
#         return contacts.scalars().all()

async def update_contacts(new_text):
    """Ф-ция обновляет контакты"""

    async with AsyncSession(bind=engine) as session:
        contacts = await session.execute(select(ContactMe))
        contact = contacts.scalars().first()
        print(contact.text)
        if contact:
            contact.text = new_text
            print(contact.text)
            await session.commit()
