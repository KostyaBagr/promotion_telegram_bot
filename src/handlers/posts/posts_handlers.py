from aiogram.types import Message, CallbackQuery, InputFile
from bot_config import bot, dp
from dotenv import load_dotenv
from aiogram.dispatcher import filters
from src.handlers.posts.crud import get_posts, get_post
from src import keyboard as kb
from src.models import Post, AdditionalPost

load_dotenv()


@dp.message_handler(filters.Text('Посмотреть презентации') | filters.Command('презентации'))
async def presentation_button(message: Message):
    """Функция показывает список презентаций"""
    posts = await get_posts(Post)
    if not posts:
        await bot.send_message(message.from_user.id, "Упс! В базе данных нет ни одной презентации")
    else:

        await bot.send_message(message.from_user.id, "Выбирайте любую презентацию!", reply_markup=await kb.posts())


@dp.callback_query_handler(text_startswith="presentation_")
async def show_post_by_id(call: CallbackQuery):
    """Функция показывает презентацию по id"""
    presentation_id = call.data.split('_')[-1]
    post = await get_post(post_id=int(presentation_id), model=Post)
    await bot.send_message(call.from_user.id, post.text)

    if post.file:  # post.file - photo id
        await bot.send_photo(call.from_user.id, post.file, '')

    if post.audio:  # post.audio -  audio id
        await bot.send_audio(call.from_user.id, post.audio)


@dp.message_handler(text='Дополнительные статьи')
async def additional_posts(message: Message):
    """Ф-ция обрабатывает получение дополнительных постов"""
    posts = await get_posts(AdditionalPost)
    if not posts:
        await bot.send_message(message.from_user.id, "Упс! В базе данных нет ни одной дополнительной презентации")
    else:

        await bot.send_message(message.from_user.id, "Выбирайте любой пост!", reply_markup=await kb.additional_posts())


@dp.callback_query_handler(text_startswith="additional_post_")
async def show_additional_post_by_id(call: CallbackQuery):
    """Функция показывает презентацию по id"""
    post_id = call.data.split('_')[-1]
    post = await get_post(post_id=int(post_id), model=AdditionalPost)

    await bot.send_message(call.from_user.id, post.text)

    if post.file:  # post.file - photo id
        if post.file_type == 'photo':
            await bot.send_photo(call.from_user.id, post.file, '')
        elif post.file_type == 'audio':
            await bot.send_audio(call.from_user.id, post.file)
        else:
            pass
