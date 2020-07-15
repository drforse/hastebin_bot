import os
from aiogram_oop_framework.views import CommandView

from hastebin import Hastebin


class Paste(CommandView):
    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        rpl_m = m.reply_to_message
        if not rpl_m:
            await m.answer('Command should be a reply to text or file with code')
            return

        hastebin = Hastebin(m.bot.session)
        if rpl_m.text:
            url = await hastebin.create_paste_from_text(rpl_m.text)
        elif rpl_m.document:
            dest = await rpl_m.document.download()
            dest.close()
            with open(dest.name) as file:
                url = await hastebin.create_paste_from_file(file)
            os.remove(dest.name)
        else:
            await m.answer('Unsupported type, supported types: document, text')
            return

        await m.reply(url)
