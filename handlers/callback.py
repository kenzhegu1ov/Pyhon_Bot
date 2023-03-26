from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import random
from config import bot



async def quiz_2(call: CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('NEXT', callback_data='button_2')
    markup.add(button_1)
    question = "Дони гей?"
    answer = [
        "Да",
        "Возможно",
        "Нет",
        "Пидора ответ",
        "Yes",
        "Ты кто?",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        reply_markup=markup
    )


async def quiz_3(call: CallbackQuery):
    question = "Сколько будет 2+2??"
    answer = [
        '4',
        '8',
        '22',
        '1',
        '20',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать"
    )


async def send_memes(message: types.Message):
   photos = ['media/apython.jpg', 'media/python1.jpg', 'media/python2.jpg', 'media/python3.jpg', 'media/python4.jpg',
             'media/python5.jpg'
             ]
   random.shuffle(photos)
   with open(photos[0], 'rb') as f:
        await bot.send_photo(message.chat.id, f)



async def send_memes_command(message: types.Message):
    await send_memes(message)



def register_handlers_callback(dp: Dispatcher):
      dp.register_callback_query_handler(quiz_2, text="button_1")
      dp.register_callback_query_handler(quiz_3)
      dp.register_message_handler(send_memes_command, commands=['mem'])
