from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inline_button_football = InlineKeyboardButton('Football', callback_data='football')
inline_button_films = InlineKeyboardButton('Films', callback_data='films')
inline_kb = InlineKeyboardMarkup()
inline_kb.add(inline_button_football)
inline_kb.add(inline_button_films)