from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()


# Ваш токен бота отриманий від BotFather в Telegram
API_KEY = '6542659135:AAEsVEDtZZwwazKRnTebiS3kVDr5CzTlumk'
bot = Bot(token=API_KEY)
dp = Dispatcher(bot, storage=storage)

