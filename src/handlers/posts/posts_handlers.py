from aiogram.types import Message, CallbackQuery
from bot_config import bot, dp
import json
from src.handlers.posts.crud import get_posts
from src.handlers.posts import posts_keyboard as kb


@dp.message_handler(text="Посмотреть презентации")
async def presentation_button(message: Message):
    posts = await get_posts()
    if not posts:
        await bot.send_message(message.from_user.id, "Упс! В базе данных нет ни одной презентации")
    await bot.send_message(message.from_user.id, "Выбирайте любую презентацию!", reply_markup=await kb.posts())


@dp.callback_query_handler(text_startswith="presentation_")
async def handle_presentation_button(call: CallbackQuery):
    presentation_id = call.data.split('_')[-1]
    print(presentation_id)
    #получать данные о презентации и присылать
    await bot.send_message(call.from_user.id, f"Выбрана презентация N: {presentation_id}")
