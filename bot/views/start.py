from aiogram_oop_framework.views import CommandView


class Start(CommandView):
    commands = ['help', 'start']
    append_commands = False

    @classmethod
    async def execute(cls, m, state=None, **kwargs):
        await m.answer('Hi. I am bot for uploading your code to hatebin.com or hastebin.com, depends on your tastes!')
