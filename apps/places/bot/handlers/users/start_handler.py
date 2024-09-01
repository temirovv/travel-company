import re

from aiogram import html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from apps.places.bot.loader import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")


