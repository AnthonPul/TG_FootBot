from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import emoji
import flag

button_1 = KeyboardButton(emoji.emojize(":england: English Premier League", language='alias'))
button_2 = KeyboardButton(flag.flagize(":es: Spanish La Liga"))
button_3 = KeyboardButton(flag.flagize(":it: Italian Seria A"))
button_4 = KeyboardButton(flag.flagize(":de:German Bundesliga"))
button_5 = KeyboardButton(flag.flagize(":fr: French Liga 1"))

first_kb = ReplyKeyboardMarkup().add(button_1).add(button_2).add(button_3).add(button_4).add(button_5)





#START = ReplyKeyboardMarkup().add(first_kb)
#SECTION = InlineKeyboardMarkup().add(section_buttons)
#BACK = InlineKeyboardMarkup().add(first_kb)
#HELP = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND).add(BTN_SUN_TIME)