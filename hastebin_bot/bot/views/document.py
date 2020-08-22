import os
from aiogram_oop_framework.views import DocumentView

from hastebin_bot.pastebin.hatebin import Hatebin


class MyDocView(DocumentView):
    index = 3
    custom_filters = [lambda m: m.chat.type == 'private']

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        pastebin = Hatebin(m.bot.session)
        dest = await m.document.download()
        dest.close()
        with open(dest.name) as file:
            url = await pastebin.create_paste_from_file(file)
        os.remove(dest.name)
        await m.reply(url)
