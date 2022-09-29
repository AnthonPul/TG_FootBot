from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



liga_1_table = KeyboardButton("Table")
liga_1_team = KeyboardButton("Team")
liga_1_schedule = KeyboardButton("Schedule")
back_button = KeyboardButton("Back")


section_keyboard_liga_1 = ReplyKeyboardMarkup().add(liga_1_table).add(liga_1_table).add(liga_1_table).add(back_button)