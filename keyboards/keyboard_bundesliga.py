from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



bundesliga_table = KeyboardButton("Table")
bundesliga_team = KeyboardButton("Team")
bundesliga_schedule = KeyboardButton("Schedule")
back_button = KeyboardButton("Back")


section_keyboard_bundesliga = ReplyKeyboardMarkup().add(bundesliga_table).add(bundesliga_table).add(bundesliga_table).add(back_button)