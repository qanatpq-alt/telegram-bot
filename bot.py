from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "8690485368:AAH0EC-jP-b_obZzqu-atRtpWMjp0Bx7_X0"
KEY = "adminkey1"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Start команда
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("🔐 Please enter your key:")

# Кілт тексеру
@dp.message_handler()
async def check_key(msg: types.Message):
    if msg.text == KEY:
        await msg.answer("✅ Correct key! Welcome!")
    else:
        await msg.answer("❌ Wrong key! Try again.")

executor.start_polling(dp)
