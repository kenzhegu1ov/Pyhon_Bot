import openai
import aiogram.utils.markdown as md
from aiogram import types
from config import API_TOKEN

openai.api_key = API_TOKEN
model_engine = 'davinci'
openai.api_base = 'https://api.openai.com/v1'


async def get_chat_gpt_answer(message_text: str) -> str:
    prompt = f'Conversation with a user:\nUser: {message_text}\nAI:'
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )
    chat_gpt_answer = response.choices[0].text
    return chat_gpt_answer


async def handle_message(message: types.Message):
    message_text = message.text
    chat_gpt_answer = await get_chat_gpt_answer(message_text)
    await message.answer(md.text(chat_gpt_answer))
