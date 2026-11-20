import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Токен берем из переменных окружения (для безопасности)
BOT_TOKEN = os.getenv("9253645189:AAFlTINvzz-icJHk_PghLHfUFYe8rXEQwSI")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я работаю на бесплатном сервере 🚀")

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    print("Бот запущен...")
    # Запуск Long Polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
