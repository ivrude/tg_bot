from aiogram import types
from .app import dp
from .keybords import inline_kb
from .states import BotStates

@dp.message_handler(commands='themes')
async def all_themes(message: types.Message):
    await BotStates.events.set()
    await message.reply('all themes', reply_markup=inline_kb)