from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



la_liga_table = KeyboardButton("Table")
la_liga_team = KeyboardButton("Team")
la_liga_schedule = KeyboardButton("Schedule")
back_button = KeyboardButton("Back")


section_keyboard_la_liga = ReplyKeyboardMarkup().add(la_liga_table).add(la_liga_table).add(la_liga_table).add(back_button)