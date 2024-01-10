from bot_config import dp, Bot, TOKEN
import logging
import asyncio
import sys

from src.handlers.users import user_handlers
from aiogram.enums import ParseMode

async def main() -> None:
    bot = Bot(TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())