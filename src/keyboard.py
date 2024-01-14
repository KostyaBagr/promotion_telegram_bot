from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from src.handlers.posts.crud import get_posts, get_additional_posts


async def start_buttons():
    """Кнопки, которые показываются при команде start"""
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    presentations = KeyboardButton(text='Посмотреть презентации')
    download = KeyboardButton(text='Скачать Gem4Me')
    referral_link = KeyboardButton(text='Стать партнером (реферальная ссылка)')
    admin_contact = KeyboardButton(text='Связаться с менеджером')
    additional_posts = KeyboardButton(text='Дополнительная информация')

    menu.add(presentations, download, admin_contact, referral_link, additional_posts)
    return menu


async def posts():
    """Презентации"""
    posts_kb = InlineKeyboardMarkup(row_width=3)
    posts_list = await get_posts()
    for post in posts_list:
        posts_kb.insert(KeyboardButton(text=f"Презентация - {post.name}", callback_data=f'presentation_{post.id}'))
    return posts_kb


async def additional_posts():
    """Дополнительный посты"""
    posts_kb = InlineKeyboardMarkup(row_width=3)
    posts_list = await get_additional_posts()
    for id, post in enumerate(posts_list, start=1):
        posts_kb.insert(KeyboardButton(text=f"Презентация N - {id}", callback_data=f'additional_post_{post.id}'))
    return posts_kb
