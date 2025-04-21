import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.reply("Привет! Отправь мне IP, номер телефона или email для анализа.")

@dp.message_handler()
async def analyze_input(message: Message):
    user_input = message.text.strip()
    # Заглушка анализа
    await message.reply(f"Анализирую: {user_input}\n(эта часть будет дописана позже)")

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
