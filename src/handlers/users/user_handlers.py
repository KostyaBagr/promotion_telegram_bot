from aiogram.types import Message
from src.handlers.users import user_keyboard as key
from sqlalchemy import select
from aiogram.filters import CommandStart
from bot_config import dp, bot

from database_config import engine
from src.handlers.users.crud import create_user
from src.models import User
from sqlalchemy.ext.asyncio import AsyncSession


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    async with AsyncSession(bind=engine) as session:
        res = await session.execute(select(User).where(User.username == message.from_user.username))
        user = res.scalar()
        if user:
            pass
        else:
            user_data = {
                "name": message.from_user.first_name,
                "username": message.from_user.username
            }

            await create_user(db=session, data=user_data)
        await bot.send_message(message.from_user.id, "Приветсвуем вас, выбирите подхоядщую для вас кнопку",
                               reply_markup=key.start_buttons())
    await session.close()
