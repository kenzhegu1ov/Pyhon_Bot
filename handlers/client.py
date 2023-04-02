import io

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from aiogram.dispatcher import FSMContext
from config import bot
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random
from parser.laptops import parser


async def start_command(message: types.Message):
    await message.answer(f'Салам алейкум {message.from_user.full_name}', reply_markup=start_markup)



async def help_command(message: types.Message):
    await message.answer("Иди на )(уй")


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Как зовут преподавателя?"
    answer = [
        "Питер Паркер",
        "Садыр Жапаров",
        "Леонардо да Винчи",
        "Барри Аллен",
        "Эсенбек Саматович",
        "Не знаю",
        "Какая разница?"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="*Преподаватель обиделся на вас*",
        reply_markup=markup
    )

async def get_random_user(message: types.Message):
    random_user = await sql_command_random()
    await message.answer_photo(
        caption=f"{random_user[1]} {random_user[2]} {random_user[3]} {random_user[4]}")


async def get_laptops(message: types.Message):
    laptops = parser()
    count = 0
    for laptop in laptops:
        count += 1
        if count == 5:
            break
        await message.answer(
            f"<b><a href='{laptop['link']}'>{laptop['description']}</a></b>\n"
            f"#{laptop['price']}",
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("ОБЗОР", url=laptop['link'])
            ),
            parse_mode=ParseMode.HTML
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(get_laptops, commands=['laptop'])

