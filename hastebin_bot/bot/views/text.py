from aiogram import Router
from aiogram.types import Message

from ...pastebin.hatebin import Hatebin


router = Router()


@router.message(lambda m: m.chat.type == "private")
async def process_document(m: Message):
    async with Hatebin() as hatebin:
        url = await hatebin.create_paste_from_text(m.text)
    await m.reply(url)
