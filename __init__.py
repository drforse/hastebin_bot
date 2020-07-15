from aiogram import Dispatcher, Bot, executor

from bot.manage import initialize_project
from bot.settings import TELEGRAM_BOT_TOKEN


if __name__ == '__main__':
    bot = Bot(TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(bot)
    initialize_project(dp, bot)
    executor.start_polling(dp)
