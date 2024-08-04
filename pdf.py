# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/pdf.py"

from configs.config import bot
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# GLOBAL VARIABLES
PDF = {}  # save images for generating pdf
works = {"u": [], "g": []}  # broken works

# Initialize bot and dispatcher
pyTgLovePDF = Bot(token=bot.API_TOKEN, parse_mode="Markdown")
dp = Dispatcher(pyTgLovePDF)


async def on_startup(_):
    print('Bot is online')

# Start polling
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
