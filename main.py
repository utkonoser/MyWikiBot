
from aiogram import Bot, Dispatcher, executor

import handlers

API_TOKEN = ''


bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

dp.register_message_handler(handlers.start,commands=["start"])

dp.register_message_handler(handlers.help,commands=["help"])

dp.register_message_handler(handlers.language_ru,commands=["language_ru"])

dp.register_message_handler(handlers.language_en,commands=["language_en"])

dp.register_message_handler(handlers.search)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)