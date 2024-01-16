from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from dotenv import load_dotenv
from bot_config import dp, bot
from src.handlers.admin.states import FSMPost, FSMAdditionalPost
from .crud import is_admin, save_admin_post
from aiogram import filters
from src import keyboard as kb
from ...models import Post, AdditionalPost

load_dotenv()


@dp.message_handler(text="Отмена", state="*")
async def cancel_create_post(message: Message, state: FSMContext):
    if await is_admin(message.from_user.id):
        curr_state = await state.get_state()
        if curr_state is None:
            return
        await state.finish()
        await message.reply('Создание поста отменено', reply_markup=await kb.admin_keyboard())


@dp.message_handler(filters.Text('Админка', ignore_case=True) | filters.Command('admin'))
async def admin_panel(message: Message):
    if await is_admin(message.from_user.id):
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, Привет, вы в админ-панеле',
                               reply_markup=await kb.admin_keyboard())


# ------------------Posts----------------------#

@dp.message_handler(text='Создать презентацию', state=None)
async def create_post_start(message: Message):
    """Добавляем презентацию. Первый шаг FSM"""
    if await is_admin(message.from_user.id):
        await FSMPost.name.set()
        await message.reply("Напишите имя для презентации", reply_markup=kb.cancel_btn)


@dp.message_handler(content_types=['text'], state=FSMPost.name)
async def get_post_name(message: Message, state: FSMContext):
    """Просим у пользователя название презентации. Второй шаг FSM"""
    if await is_admin(message.from_user.id):
        if message.text == "Следующий шаг":
            await message.reply("Поле \"имя\" не должно быть пустым.")
        if len(message.text) > 30:
            await message.reply('Поле "Имя" не должно состоять более, чем из 30 символов.\n'
                                'Пожалуйста, сделайте свой текст короче и попробуйте снова')
        else:
            async with state.proxy() as data:
                data['name'] = message.text
            await FSMPost.next()
            await message.reply("Напишите текст для презентации", reply_markup=kb.cancel_btn)


@dp.message_handler(content_types=['text'], state=FSMPost.text)
async def get_post_text(message: Message, state: FSMContext):
    """Просим у пользователя тест для презентации. Третий шаг FSM"""
    if await is_admin(message.from_user.id):
        if message.text == "Следующий шаг":
            await message.reply("Поле \"текст\" не должно быть пустым.")
        else:
            async with state.proxy() as data:
                data['text'] = message.text
            await FSMPost.next()
            await message.reply("Отправьте фото для презентации (если это необходимо)",
                                reply_markup=await kb.next_or_cancel_post())


@dp.message_handler(content_types=['photo'], state=FSMPost.file)
async def get_post_file(message: Message, state: FSMContext):
    """Просим у пользователя файл(фото) для презентации. Четвертый шаг FSM"""
    if await is_admin(message.from_user.id):
        async with state.proxy() as data:
            data['file'] = message.photo[0].file_id
        await FSMPost.next()
        await message.reply("Отправьте аудио для презентации(если это необходимо)",
                            reply_markup=await kb.next_or_cancel_post())


@dp.message_handler(text="Следующий шаг", state=FSMPost.file)
async def process_next_step(message: Message, state: FSMContext):
    """Обработчик кнопки "Следующий шаг" на четвертом шаге FSM"""
    if await is_admin(message.from_user.id):
        await FSMPost.next()
        await message.reply("Отправьте аудио для презентации (если это необходимо)",
                            reply_markup=await kb.next_or_cancel_post())


@dp.message_handler(content_types=['audio', 'voice'], state=FSMPost.audio)
async def get_post_audio(message: Message, state: FSMContext):
    """Просим у пользователя аудио для презентации. Пятый шаг FSM"""
    if await is_admin(message.from_user.id):

        audio = message.audio or message.voice
        if audio:
            async with state.proxy() as data:
                data['audio'] = audio.file_id
            await save_admin_post(state, Post)
            await state.finish()
            await message.reply("Спасибо, на этом все", reply_markup=await kb.admin_keyboard())
        else:
            await message.reply("Пожалуйста, отправьте аудиофайл")


@dp.message_handler(text="Следующий шаг", state=FSMPost.audio)
async def process_next_step_audio(message: Message, state: FSMContext):
    """Обработчик кнопки 'Следующий шаг' на пятом шаге FSM"""
    if await is_admin(message.from_user.id):
        await save_admin_post(state, Post)
        await state.finish()
        await message.reply("Спасибо, на этом все", reply_markup=await kb.admin_keyboard())


# ------------------Additional posts----------------------#


@dp.message_handler(text='Создать дополнительную статью', state=None)
async def create_additional_post_start(message: Message):
    """Добавляем доп. статью. Первый шаг FSM"""
    if await is_admin(message.from_user.id):
        await FSMAdditionalPost.text.set()
        await message.reply("Добавьте текст к статье или нажмите \"Следующий шаг\", чтобы пропустить этот шаг",
                            reply_markup=await kb.next_or_cancel_post())


@dp.message_handler(content_types=['text'], state=FSMAdditionalPost.text)
async def get_additional_post_text(message: Message, state: FSMContext):
    """Просим у пользователя текст стаьи Второй шаг FSM"""
    if await is_admin(message.from_user.id):
        async with state.proxy() as data:
            data['text'] = message.text
        await FSMAdditionalPost.next()
        await message.reply(
            "Добавьте фото или аудио к статье или нажмите \"Следующий шаг\", чтобы пропустить этот шаг",
            reply_markup=await kb.next_or_cancel_post())


@dp.message_handler(text="Следующий шаг", state=FSMAdditionalPost.text)
async def next_step_text(message: Message, state: FSMContext):
    """Обработчик кнопки "Следующий шаг" для текста FSM"""
    if await is_admin(message.from_user.id):
        await FSMAdditionalPost.next()
        await message.reply("Добавьте фото или аудио к статье или нажмите \"Следующий шаг\", чтобы пропустить этот шаг",
                            reply_markup=await kb.next_or_cancel_post())


@dp.message_handler(content_types=['audio', 'voice', 'photo'], state=FSMAdditionalPost.file)
async def get_additional_post_file(message: Message, state: FSMContext):
    """Просим у пользователя файл для презентации. Третий шаг FSM"""
    if await is_admin(message.from_user.id):
        async with state.proxy() as data:
            if message.content_type == 'photo':
                data['file'], data['file_type'] = message.photo[0]['file_id'], 'photo'
            elif message.content_type == 'audio':
                data['file'], data['file_type'] = message.audio['file_id'], 'audio'
            elif message.content_type == 'voice':
                data['file'], data['file_type'] = message.voice['file_id'], 'audio'
            else:
                await message.reply('Неизвестный тип данных')
        await save_admin_post(state, AdditionalPost)
        await state.finish()
        await message.reply("Спасибо, вы успешно создали новую статью", reply_markup=await kb.admin_keyboard())


@dp.message_handler(text="Следующий шаг", state=FSMAdditionalPost.file)
async def next_step_file(message: Message, state: FSMContext):
    """Обработчик кнопки "Следующий шаг" для текста FSM"""
    if await is_admin(message.from_user.id):
        await save_admin_post(state, AdditionalPost)
        await state.finish()
        await message.reply("Спасибо, вы успешно создали новую статью",
                            reply_markup=await kb.admin_keyboard())
