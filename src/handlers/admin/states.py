from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMPost(StatesGroup):
    """FSM для добавления поста"""
    name = State()
    text = State()
    file = State()
    audio = State()


class FSMAdditionalPost(StatesGroup):
    """FSM для добавления дополнительных постов"""
    text = State()
    file = State()
