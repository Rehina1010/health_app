from config.config import config

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


TOKEN = config["BOT_TOKEN"]
print(TOKEN)
# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))