import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from django.conf import settings


bot = Bot(token=settings.BOT_API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def main() -> None:
    await dp.start_polling(bot)


def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
