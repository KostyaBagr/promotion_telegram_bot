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


async def admin_keyboard():
    """Кнопки для админки """
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    create_post = KeyboardButton(text='Создать презентацию')
    create_additional_post = KeyboardButton(text='Создать дополнительный пост')
    referral_links = KeyboardButton(text='Добавить реферальную ссылку')
    contact_me = KeyboardButton(text='Добавить контакты для связи')

    admin_kb.add(create_post, create_additional_post, referral_links, contact_me)
    return admin_kb


async def next_or_cancel_post():
    """Кнопки отмены и далее"""
    post_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    cancel = KeyboardButton(text="Отмена")
    next= KeyboardButton(text='Следующий шаг')
    post_kb.add(next, cancel)
    return post_kb

cancel_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Отмена"))
