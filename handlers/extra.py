
from aiogram import types, Dispatcher
from handlers.gpt import handle_message


async def handle_all_messages(message: types.Message):
    await handle_message(message)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(handle_all_messages)



