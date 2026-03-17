from aiogram import Bot, Dispatcher
import asyncio
import os
import logging
from dotenv import load_dotenv
from handlers.user import user

load_dotenv()

logging.basicConfig(level=logging.DEBUG)


async def main():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(user)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Бот включён!")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен!")
