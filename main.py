from bot_config import dp, Bot, TOKEN

from aiogram import executor

from src.handlers.users import user_handlers
from src.handlers.posts import posts_handlers
from src.handlers.admin import admin_handlers


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)