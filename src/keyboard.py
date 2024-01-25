from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from src.handlers.admin.crud import is_admin, get_contacts
from src.handlers.posts.crud import get_posts
from src.models import Post, AdditionalPost


async def start_buttons():
    """Кнопки, которые показываются при команде start"""
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    presentations = KeyboardButton(text='Презентации')
    download = KeyboardButton(text='Скачать ⬇')
    referral_link = KeyboardButton(text='Стать партнером')
    admin_contact = KeyboardButton(text='Задать вопрос')
    additional_posts = KeyboardButton(text='Это интересно')

    menu.add(presentations, download,referral_link, admin_contact, additional_posts)
    return menu


async def posts(user_id):
    """Презентации"""
    posts_kb = InlineKeyboardMarkup(row_width=2)
    posts_list = await get_posts(model=Post)
    for post in posts_list:
        posts_kb.insert(KeyboardButton(text=f"Презентация - {post.name}", callback_data=f'presentation_{post.id}'))
        if await is_admin(user_id):
            posts_kb.insert(KeyboardButton(text=f"Удалить: {post.name}", callback_data=f'delete_presentation_{post.id}'))
    return posts_kb


async def additional_posts(user_id):
    """Дополнительный посты"""
    posts_kb = InlineKeyboardMarkup(row_width=2)
    posts_list = await get_posts(model=AdditionalPost)
    for id, post in enumerate(posts_list, start=1):
        posts_kb.insert(KeyboardButton(text=f"Статья N - {id}", callback_data=f'additional_post_{post.id}'))
        if await is_admin(user_id):
            posts_kb.insert(KeyboardButton(text=f"Удалить статью N - {id}", callback_data=f'delete_additional_presentation_{post.id}'))

    return posts_kb


async def admin_keyboard():
    """Кнопки для админки """
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    create_post = KeyboardButton(text='Создать презентацию')
    create_additional_post = KeyboardButton(text='Создать дополнительную статью')
    if await get_contacts():
        contact_me = KeyboardButton(text='Изменить контакты для связи')

    else:
        contact_me = KeyboardButton(text='Добавить контакты для связи')

    admin_kb.add(create_post, create_additional_post, contact_me)
    return admin_kb


async def next_or_cancel_post():
    """Кнопки отмены и далее"""
    post_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    cancel = KeyboardButton(text="Отмена")
    next= KeyboardButton(text='Следующий шаг')
    post_kb.add(cancel, next)
    return post_kb

cancel_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Отмена"))
