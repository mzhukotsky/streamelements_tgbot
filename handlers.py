from main import bot, dp
from aiogram.types import Message
from config_my import admin_id

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="БОТОЗАВР ПУЩЕН")

# @dp.message_handler()
# async def echo(message: Message):
#     print(message.text)
#     text = f"Чел, ты реально написал: {message.text}"
#     await bot.send_message(chat_id=message.from_user.id,
#                            text=text)
#     # await message.answer(text=text)
