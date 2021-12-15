import codecs
import os
from aiogram import Router, Bot
from aiogram.types import ContentType, Message

from ...pastebin.hatebin import Hatebin


router = Router()


@router.message(lambda m: m.chat.type == "private", content_types=ContentType.DOCUMENT)
async def process_document(m: Message, bot: Bot):
    dest = await bot.download(m.document)
    reader = codecs.getreader("utf-8")
    async with Hatebin() as hatebin:
        url = await hatebin.create_paste_from_file(reader(dest))
    dest.close()
    await m.reply(url)
