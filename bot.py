from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text
from keyboards import keyboards_and_buttons as kb
from football_all_data import football_data_bundesliga, football_data_seriaa, football_data_france, football_data_epl, \
    football_data_laliga

TOKEN = "5672966620:AAHsNa5f6hzflLmDDXN_QK7SBDbcXVfoopU"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello! Choice your favorite league. \nFor help enter '/help'", reply_markup=kb.first_kb)

@dp.callback_query_handler(run_task=football_data_epl)
async def process_epl_button_(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(text=football_data_epl.df_res_epl_short)
#@dp.message_handler(commands=['England'])
#async def process_epl_command(message: types.Message):
#    await message.answer(text=football_data_epl.df_res_epl_short, reply_markup=kb.epl_button)


@dp.message_handler(commands=['Spain'])
async def process_la_liga_command(message: types.Message):
    await message.answer(text=football_data_laliga.df_res_laliga_short, reply_markup=kb.la_liga_button)


@dp.message_handler(commands=['Italy'])
async def process_seria_a_command(message: types.Message):
    await message.answer(text=football_data_seriaa.df_res_italy_short, reply_markup=kb.la_liga_button)


@dp.message_handler(commands=['Germany'])
async def process_bundesliga_command(message: types.Message):
    await message.answer(text=football_data_bundesliga.df_res_bundes_short, reply_markup=kb.bundesliga_button)


@dp.message_handler(commands=['France'])
async def process_liga_1_command(message: types.Message):
    await message.answer(text=football_data_france.df_res_france_short, reply_markup=kb.liga_1_button)


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


if __name__ == "__main__":
    print("Bot started!")
    executor.start_polling(dp)
