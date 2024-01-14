from aiogram.types import Message, CallbackQuery, InputFile
from bot_config import bot, dp
from dotenv import load_dotenv
from src.handlers.posts.crud import get_posts, get_post, get_additional_post, get_additional_posts
from src import keyboard as kb

load_dotenv()


@dp.message_handler(text="Посмотреть презентации")
async def presentation_button(message: Message):
    """Функция показывает список презентаций"""
    posts = await get_posts()
    if not posts:
        await bot.send_message(message.from_user.id, "Упс! В базе данных нет ни одной презентации")
    else:

        await bot.send_message(message.from_user.id, "Выбирайте любую презентацию!", reply_markup=await kb.posts())


@dp.callback_query_handler(text_startswith="presentation_")
async def show_post_by_id(call: CallbackQuery):
    """Функция показывает презентацию по id"""
    presentation_id = call.data.split('_')[-1]
    post = await get_post(post_id=int(presentation_id))

    if post.file:  # post.file - путь, где хранится фото
        photo = InputFile(post.file)
        await bot.send_file(call.from_user.id, photo=photo)

    if post.audio:  # post.audio - путь, где хранится аудио

        with open(post.audio, mode="rb") as file:
            await bot.send_audio(chat_id=call.from_user.id, audio=file)

    await bot.send_message(call.from_user.id, post.text)


@dp.message_handler(text='Дополнительная информация')
async def additional_posts(message: Message):
    """Ф-ция обрабатывает получение дополнительных постов"""
    posts = await get_additional_posts()
    if not posts:
        await bot.send_message(message.from_user.id, "Упс! В базе данных нет ни одной дополнительной презентации")
    else:

        await bot.send_message(message.from_user.id, "Выбирайте любой пост!", reply_markup=await kb.additional_posts())


@dp.callback_query_handler(text_startswith="additional_post_")
async def show_additional_post_by_id(call: CallbackQuery):
    """Функция показывает презентацию по id"""
    post_id = call.data.split('_')[-1]
    post = await get_additional_post(post_id=int(post_id))

    if post.file:  # post.file - путь, где хранится фото
        photo = InputFile(post.file)
        await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_message(call.from_user.id, post.text)
