import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_LINK = "https://t.me/SatoriDzen"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    text = (
        "Ты стоишь в начале пути.\n\n"
        "Этот небольшой тест — не про оценки.\n"
        "Он про честный взгляд на прошедший год.\n\n"
        "Ответь на несколько вопросов,\n"
        "чтобы увидеть:\n"
        "— где был прогресс\n"
        "— где был застой\n"
        "— и куда ты на самом деле идёшь\n\n"
        "В конце тебя ждёт результат\n"
        "и приглашение сделать первый шаг\n"
        "на пути Сатори."
    )

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Начать путь",
                    callback_data="start_test"
                )
            ]
        ]
    )

    await message.answer(text, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "start_test")
async def start_test(callback: types.CallbackQuery):
    await callback.message.answer(
        "Представь:\n\n"
        "Если этот год показал,\n"
        "что ты что-то упускал —\n"
        "значит, следующий может стать точкой роста.\n\n"
        "Если ты многое сделал —\n"
        "значит, ты уже на пути.\n\n"
        "Продолжение размышлений — здесь:\n"
        f"{CHANNEL_LINK}\n\n"
        "Возможно, это и есть начало нового пути."
    )
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if name == "__main__":
    asyncio.run(main())
