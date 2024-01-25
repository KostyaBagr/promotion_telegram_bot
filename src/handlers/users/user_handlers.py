import os

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, KeyboardButton, ParseMode
from src import keyboard as kb
from bot_config import dp, bot
from dotenv import load_dotenv

from src.handlers.admin.crud import is_admin, update_contacts
from src.handlers.admin.states import FSMUpdateContact
from src.handlers.users.crud import create_user, is_user, get_contacts

load_dotenv()


@dp.message_handler(commands=['start', 'menu'])
async def command_start_handler(message: Message):
    """Ф-ция обрабатывает команду start и сохраняет пользователя в БД"""
    print('start', message.from_user.username)
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


@dp.message_handler(text='Скачать ⬇🔄')
async def download_gem4me(message: Message):
    """Ф-ция обрабатывает кнопку Скачать Gem4Me"""
    await bot.send_message(message.from_user.id,
                           f"Наша маркетинговая команда в 2023 году полностью изменила лицо нашего проекта, то есть провела полный ребрендинг. Наш главный сайт, который теперь, естественно, называет gemspace.com, отражает те глобальные изменения, которые уже произошли в проекте, и которые мы увидим в ближайшие месяцы.",
                           disable_web_page_preview=True)


@dp.message_handler(text='Стать партнером')
async def referral_link(message: Message):
    """Ф-ция обрабатывает кнопку 'Стать партнером' и присылает реферальные ссылки"""

    await bot.send_message(message.from_user.id,
                           f'Реферальная ссылка - <a href="http://bc.gem4me.com/session/signup?sponsor=cuchum">перейти</a>',
                           parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@dp.message_handler(text='Задать вопрос')
async def contact_admin(message: Message):
    """Ф-ция обрабатывает кнопку 'Стать партнером' и присылает реферальные ссылки"""

    contact = await get_contacts()
    if contact:
        await bot.send_message(message.from_user.id, f'Контакты для связи: \n\n{contact.text}',
                               disable_web_page_preview=True)
    else:
        await bot.send_message(message.from_user.id, "К сожалению контактов для связи нет")



