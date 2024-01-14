import os
from aiogram.types import Message, CallbackQuery, KeyboardButton
from src import keyboard as kb
from bot_config import dp, bot
from dotenv import load_dotenv
from src.handlers.users.crud import create_user, is_user, get_referral_links, get_contacts

load_dotenv()


@dp.message_handler(commands=['start'])
async def command_start_handler(message: Message) -> None:
    """Ф-ция обрабатывает команду start и сохраняет пользователя в БД"""
    user = await is_user(telegram_id=message.from_user.id)
    if not user:
        user_data = {
            "name": message.from_user.first_name,
            "username": message.from_user.username,
            "telegram_id": message.from_user.id
        }

        await create_user(data=user_data)
    await bot.send_message(message.from_user.id, "Приветсвуем вас, выбирите подхоядщую для вас кнопку",
                           reply_markup=await kb.start_buttons())


@dp.message_handler(text='Скачать Gem4Me')
async def download_gem4me(message: Message):
    """Ф-ция обрабатывает кнопку Скачать Gem4Me"""
    await bot.send_message(message.from_user.id, f"Скачать приложение - {os.getenv('DOWNLOAD_LINK')}", disable_web_page_preview=True)


@dp.message_handler(text='Стать партнером (реферальная ссылка)')
async def referral_link(message: Message):
    """Ф-ция обрабатывает кнопку 'Стать партнером' и присылает реферальные ссылки"""

    links = await get_referral_links()
    for link in links:
        await bot.send_message(message.from_user.id, f'Реферальная ссылка - {link.link}', disable_web_page_preview=True)


@dp.message_handler(text='Связаться с менеджером')
async def contact_admin(message: Message):
    """Ф-ция обрабатывает кнопку 'Стать партнером' и присылает реферальные ссылки"""

    contact = await get_contacts()
    for c in contact:
        await bot.send_message(message.from_user.id, f'Контакты для связи: \n\n{c.text}', disable_web_page_preview=True)
