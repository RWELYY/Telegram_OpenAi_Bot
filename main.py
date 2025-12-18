import os
import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from openai import OpenAI

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
client = OpenAI(api_key=OPENAI_KEY)


@dp.message()
async def chat(message: types.Message):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": message.text}
            ],
        )

        await message.answer(response.choices[0].message.content)

    except Exception as e:
        await message.answer("error")
        print(e)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
