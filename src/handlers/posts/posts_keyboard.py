from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from src.handlers.posts.crud import get_posts


async def posts():
    posts_kb = InlineKeyboardMarkup(row_width=3)
    posts_list = await get_posts()
    for idx, post in enumerate(posts_list, start=1):
        posts_kb.insert(KeyboardButton(text=f"Презентация N: {idx}", callback_data=f'presentation_{post.id}'))
    return posts_kb
