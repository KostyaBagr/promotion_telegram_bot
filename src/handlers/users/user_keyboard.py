from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


async def start_buttons():
    """Кнопки, которые показываются при команде start"""
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    presentations = KeyboardButton(text='Посмотреть презентации')
    registration = KeyboardButton(text='Зарегистрироваться')
    admin_contact = KeyboardButton(text='Связаться со мной')
    not_interesting = KeyboardButton(text='Мне неинтересно')

    menu.add(presentations, registration, admin_contact, not_interesting)
    return menu

