from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(commands=["start"])
async def start(m: Message):
    await m.answer('Hi. I am bot for uploading your code to hatebin.com or hastebin.com, depends on your tastes!')
