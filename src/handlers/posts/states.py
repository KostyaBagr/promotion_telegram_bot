from aiogram.dispatcher.filters.state import StatesGroup, State


class AddPost(StatesGroup):
    """FSM для добавления поста в админ панеле"""
    text = State()
    audio = State()
    file = State()