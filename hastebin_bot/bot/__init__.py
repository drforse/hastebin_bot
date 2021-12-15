from . views import routers as msg_routers
from .views.commands import routers as cmd_routers

from aiogram import Dispatcher, Bot

from .settings import TELEGRAM_BOT_TOKEN


all_routers = cmd_routers + msg_routers


async def run_polling():
    dp = Dispatcher()
    for router in all_routers:
        dp.include_router(router)
    bot = Bot(TELEGRAM_BOT_TOKEN)
    await dp.start_polling(bot)
