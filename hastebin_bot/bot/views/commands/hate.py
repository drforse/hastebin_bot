import codecs
from aiogram import Router, Bot
from aiogram.types import Message

from ....pastebin.hastebin import Hastebin
from ....pastebin.hatebin import Hatebin


router = Router()


@router.message(commands=["hate", "haste"])
async def hate_haste(m: Message, bot: Bot):
    rpl_m = m.reply_to_message
    if not rpl_m:
        await m.answer('Command should be a reply to text or file with code')
        return

    if m.text.startswith('/hate'):
        pastebin = Hatebin()
    else:
        pastebin = Hastebin()
    if rpl_m.text:
        url = await pastebin.create_paste_from_text(rpl_m.text)
    elif rpl_m.document:
        dest = await bot.download(rpl_m.document)
        reader = codecs.getreader("utf-8")
        url = await pastebin.create_paste_from_file(reader(dest))
        dest.close()
    else:
        await m.answer('Unsupported type, supported types: document, text')
        return

    await pastebin.disconnect()
    await m.reply(url)
