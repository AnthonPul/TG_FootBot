from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton




section_button_1 = KeyboardButton("Table")
section_button_2 = KeyboardButton("Team")
section_button_3 = KeyboardButton("Schedule")
section_button_4 = KeyboardButton("Back")

section_buttons = ReplyKeyboardMarkup().add(section_button_1).add(section_button_2).add(section_button_3).add(section_button_4)