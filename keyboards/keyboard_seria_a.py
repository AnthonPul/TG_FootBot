from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



seria_a_table = KeyboardButton("Table")
seria_a_team = KeyboardButton("Team")
seria_a_schedule = KeyboardButton("Schedule")
back_button = KeyboardButton("Back")


section_keyboard_seria_a = ReplyKeyboardMarkup().add(seria_a_table).add(seria_a_table).add(seria_a_table).add(back_button)