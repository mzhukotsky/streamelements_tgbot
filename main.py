import requests
import asyncio

from aiogram import Bot, Dispatcher, executor
from config_my import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)



# response = requests.get('https://api.streamelements.com/kappa/v2/store/61e8d63d3d12f65a5584b351/items')
# response_json = response.json()
#
# for game in response_json:
#     name = game.get('name')
#     cost = game.get('cost')
#     images = game.get('thumbnail')
#     print(f"name - {name}\ncost - {cost}\nimages - {images}\n")
#     # pprint(game)


