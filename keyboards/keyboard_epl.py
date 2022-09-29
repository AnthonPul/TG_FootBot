from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



epl_table = KeyboardButton("Table")
epl_teams = KeyboardButton("Team")
epl_schedule = KeyboardButton("Schedule")
back_button = KeyboardButton("Back")


section_keyboard_epl = ReplyKeyboardMarkup().add(epl_table).add(epl_teams).add(epl_schedule).add(back_button)