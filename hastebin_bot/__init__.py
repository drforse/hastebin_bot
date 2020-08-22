from aiogram import Dispatcher, Bot, executor

from hastebin_bot.bot.manage import initialize_project
from hastebin_bot.bot.settings import TELEGRAM_BOT_TOKEN


def main():
    bot = Bot(TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(bot)
    initialize_project(dp, bot)
    executor.start_polling(dp)
