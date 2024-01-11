from aiogram.types import Message, CallbackQuery
from src.handlers.users import user_keyboard as key
from sqlalchemy import select

from bot_config import dp, bot

from database_config import engine
from src.handlers.users.crud import create_user, is_user
from src.models import User, Post
from sqlalchemy.ext.asyncio import AsyncSession


@dp.message_handler(commands=['start'])
async def command_start_handler(message: Message) -> None:
    user = await is_user(telegram_id=message.from_user.id)
    if not user:
        user_data = {
            "name": message.from_user.first_name,
            "username": message.from_user.username,
            "telegram_id": message.from_user.id
        }

        await create_user(data=user_data)
    await bot.send_message(message.from_user.id, "Приветсвуем вас, выбирите подхоядщую для вас кнопку",
                           reply_markup=await key.start_buttons())





