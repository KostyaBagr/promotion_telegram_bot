from aiogram.types import Message, ParseMode
from dotenv import load_dotenv
from bot_config import dp, bot
from src.models import User, Post, AdditionalPost
import os
from .crud import is_admin, AdminReport
from aiogram import filters

load_dotenv()


@dp.message_handler(filters.Text('Админка') | filters.Command('admin'))
async def admin_panel(message: Message):
    report = AdminReport()

    if await is_admin(message.from_user.id):
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, Привет, вы в админ-панеле')
        await bot.send_message(message.from_user.id, f'ОТЧЕТ:\n\n'
                                                     f'Кол-во пользователей: {await report.count_objects(User)}\n'
                                                     f'Кол-во презентаций: {await report.count_objects(Post)}\n'
                                                     f'Кол-во дополнительных постов: {await report.count_objects(AdditionalPost)}')
