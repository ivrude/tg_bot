from aiogram.dispatcher.filters.state import State, StatesGroup

class BotStates(StatesGroup):
    start = State()
    themes = State()
    events = State()