# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/pdf.py"

from configs.config import bot
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# GLOBAL VARIABLES
PDF = {}  # save images for generating pdf
works = {"u": [], "g": []}  # broken works

# Initialize bot and dispatcher
pyTgLovePDF = Bot(token=bot.API_TOKEN, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm your bot!\nPowered by aiogram.")

async def on_startup(dp):
    await pyTgLovePDF.send_message(chat_id=YOUR_CHAT_ID, text="Bot is online")

# Start polling
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
