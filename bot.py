from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text
from keyboards import keyboards_and_buttons as kb
from keyboards import keyboards_sections as kb_sect
from keyboards import keyboard_epl as kb_epl
from keyboards import keyboard_seria_a as kb_s_a
from keyboards import keyboard_la_liga as kb_la_liga
from keyboards import keyboards_liga_1 as kb_liga_1
from keyboards import keyboard_bundesliga as kb_budnes


TOKEN = "5672966620:AAHsNa5f6hzflLmDDXN_QK7SBDbcXVfoopU"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello! Choice your favorite league. \nFor help enter '/help'", reply_markup=kb.first_kb)


@dp.message_handler(commands=['epl'])
async def process_start_command(message: types.Message):
    await message.reply("Select necessary section", reply_markup=kb_epl.section_keyboard_epl)

@dp.message_handler(run_task=kb.button_1)
async def select_section(message: types.Message):
    await message.reply("Select necessary section", reply_markup=kb_epl.section_keyboard_epl)


@dp.message_handler(commands=['spain'])
async def process_start_command(message: types.Message):
    await message.reply("Select necessary section", reply_markup=kb_la_liga.section_keyboard_la_liga)

@dp.message_handler(run_task=kb.button_2)
async def select_section(message: types.Message):
    await message.reply("Select necessary section", reply_markup=kb_la_liga.section_keyboard_la_liga)

@dp.message_handler(commands=['italy'])
async def process_start_command(message: types.Message):
    await message.reply("Select necessary section", reply_markup=kb_s_a.section_keyboard_seria_a)

@dp.message_handler(run_task=kb.button_3)
async def select_section(message: types.Message):
    await message.reply("Select necessary section", reply_markup=kb_s_a.section_keyboard_seria_a)


@dp.message_handler(commands=['germany'])
async def process_start_command(message: types.Message):
    await message.reply("Select necessary section", reply_markup=kb_budnes.section_keyboard_bundesliga)

@dp.message_handler(run_task=kb.button_4)
async def select_section(message: types.Message):
    await message.reply("Select necessary section", reply_markup=kb_budnes.section_keyboard_bundesliga)


@dp.message_handler(commands=['france'])
async def process_start_command(message: types.Message):
    await message.reply("Select necessary section", reply_markup=kb_liga_1.section_keyboard_liga_1)

@dp.message_handler(run_task=kb.button_5)
async def select_section(message: types.Message):
    await message.reply("Select necessary section", reply_markup=kb_liga_1.section_keyboard_liga_1)

@dp.message_handler(commands=['back'])
async def back_button(message: types.Message):
    await message.answer("Choice your favorite league.", reply_markup=kb_sect.section_button_4)

help_message = text(
    "List of commands:\n"
    "/start - Start \n"
    "/England - England Premier League \n"
    "/Spain - Spanish La Liga \n"
    "/Italy - Italian Seria A \n"
    "/Germany - German Bundesliga \n"
    "/France - French Liga 1 \n"
    "/help - Help"
)
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)



#@dp.inline_handler(kb.button_1)
#async def epl_section_buttons(callback_query: types.CallbackQuery):
 #   await bot.send_message("Select necessary section")






if __name__ == "__main__":
    print("Bot started!")
    executor.start_polling(dp)