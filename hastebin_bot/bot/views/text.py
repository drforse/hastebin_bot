from aiogram_oop_framework.views import TextView

from hastebin_bot.pastebin.hatebin import Hatebin


class MyTextView(TextView):
    index = 2
    custom_filters = [lambda m: m.chat.type == 'private']

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        pastebin = Hatebin(m.bot.session)
        url = await pastebin.create_paste_from_text(m.text)
        await m.reply(url)
