import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.redis import RedisStorage2

load_dotenv()


storage = RedisStorage2(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT"))
)
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

