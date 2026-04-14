from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import time

TOKEN = "8690485368:AAH0EC-jP-b_obZzqu-atRtpWMjp0Bx7_X0"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# 🔑 КЛЮЧТАР (күн саны)
keys = {
    # 1 күн (15 ключ)
    "day1_a1": 1, "day1_a2": 1, "day1_a3": 1, "day1_a4": 1, "day1_a5": 1,
    "day1_a6": 1, "day1_a7": 1, "day1_a8": 1, "day1_a9": 1, "day1_a10": 1,
    "day1_a11": 1, "day1_a12": 1, "day1_a13": 1, "day1_a14": 1, "day1_a15": 1,

    # 15 күн (10 ключ)
    "day15_b1": 15, "day15_b2": 15, "day15_b3": 15, "day15_b4": 15, "day15_b5": 15,
    "day15_b6": 15, "day15_b7": 15, "day15_b8": 15, "day15_b9": 15, "day15_b10": 15,

    # 30 күн (10 ключ)
    "month_c1": 30, "month_c2": 30, "month_c3": 30, "month_c4": 30, "month_c5": 30,
    "month_c6": 30, "month_c7": 30, "month_c8": 30, "month_c9": 30, "month_c10": 30,

    # 1 жыл (5 ключ)
    "year_d1": 365, "year_d2": 365, "year_d3": 365, "year_d4": 365, "year_d5": 365,
}

# 👤 Пайдаланушылар
users = {}

# 🚀 /start
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    user_id = msg.from_user.id

    if user_id in users:
        if users[user_id] > time.time():
            days_left = int((users[user_id] - time.time()) / 86400)
            await msg.answer(f"✅ Сенде доступ бар\n⏳ Қалған күн: {days_left}")
        else:
            await msg.answer("❌ Уақытың бітті\n🔑 Қайтадан ключ енгіз:")
    else:
        await msg.answer("🔑 Ключ енгіз:")

# 🔑 Ключ тексеру
@dp.message_handler()
async def check_key(msg: types.Message):
    user_id = msg.from_user.id
    text = msg.text

    if text in keys:
        days = keys[text]
        users[user_id] = time.time() + (days * 86400)

        # қолданылған ключты өшіру
        del keys[text]

        await msg.answer(f"✅ Доступ ашылды!\n📅 {days} күнге")
    else:
        await msg.answer("❌ Қате ключ!")

# 🚀 RUN
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
