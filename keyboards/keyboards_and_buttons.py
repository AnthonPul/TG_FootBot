from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import emoji
import flag

epl_button = InlineKeyboardButton(emoji.emojize(":england: England", language='alias'), callback_data='England')
la_liga_button = InlineKeyboardButton(flag.flagize(":es: Spain"), callback_data='Spain')
seria_a_button = InlineKeyboardButton(flag.flagize(":it: Italy"), callback_data='Germany')
bundesliga_button = InlineKeyboardButton(flag.flagize(":de: Germany"), callback_data='Italy')
liga_1_button = InlineKeyboardButton(flag.flagize(":fr: France"), callback_data='France')

first_kb = InlineKeyboardMarkup().add(epl_button).add(la_liga_button).add(seria_a_button).add(bundesliga_button).add(
    liga_1_button)

