from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ParseMode
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINS
from keyboards import client_kb
from database.bot_db import sql_command_insert
class Mentor(StatesGroup):
    mentor_id = State()
    mentor_name = State()
    mentor_direction = State()
    mentor_age = State()
    mentor_group = State()
    submit = State()


async def add_mentor(message: types.Message):
    await Mentor.mentor_id.set()
    await message.reply("Введите ID ментора", reply_markup=client_kb.cancel_markup)



async def process_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
    await Mentor.next()
    await message.reply("Введите имя ментора", reply_markup=client_kb.cancel_markup)




async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Mentor.next()
    await message.reply("Введите направление ментора", reply_markup=client_kb.cancel_markup)


async def process_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await Mentor.next()
    await message.reply("Введите возраст ментора", reply_markup=client_kb.cancel_markup)



async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числами!")
    elif int(message.text) < 16 or int(message.text) > 40:
        await message.answer("Возрастное ограничение")

    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await Mentor.next()
        await message.reply("Введите группу ментора", reply_markup=client_kb.cancel_markup)



async def process_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await state.finish()
        await message.reply(
            f"ID ментора: {data['id']}\n"
            f"Имя ментора: {data['name']}\n"
            f"Направление ментора: {data['direction']}\n"
            f"Возраст ментора: {data['age']}\n"
            f"Группа ментора: {data['group']}",
            parse_mode=ParseMode.HTML
        )
        await Mentor.next()
        await message.answer("Все верно?", reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text == "ДА":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Ты зареган!")
    elif message.text == "НЕТ":
        await state.finish()
        await message.answer("Ну и пошел ты!")
    else:
        await message.answer("Нормально пиши!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Отменено")


def register_handlers_fsm_admin_mentor(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals="cancel", ignore_case=True), state='*')
    dp.register_message_handler(add_mentor, commands=['mentor'])
    dp.register_message_handler(process_id, state=Mentor.mentor_id)
    dp.register_message_handler(process_name, state=Mentor.mentor_name)
    dp.register_message_handler(process_direction, state=Mentor.mentor_direction)
    dp.register_message_handler(process_age, state=Mentor.mentor_age)
    dp.register_message_handler(process_group, state=Mentor.mentor_group)
    dp.register_message_handler(submit, state=Mentor.submit)