from aiogram import types
from .app import *
from .keybords import inline_kb
from .states import BotStates
from .data_fetcher import get_all
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands='football',state='*')
async def get_all(message: types.Message, state: FSMContext):
    await BotStates.events.set()
    res = await get_all()
    async with state.proxy() as data:
        data['answer'] = res['title']
        data['description'] = res['description']

        await message.reply(f"{data['answer']} and {data['description']} ", reply_markup=inline_kb)
