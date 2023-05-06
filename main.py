from aiogram import Bot, Dispatcher
from aiogram.enums import ContentType
from aiogram.filters import Command, or_f, Text, invert_f, and_f
from aiogram.types import Message
import os
from dotenv import load_dotenv, find_dotenv
from aiogram import F
from environs import Env


env = Env()              # Создаем экземпляр класса Env
env.read_env()
BOT_TOKEN: str = env("TOKEN")

# load_dotenv(find_dotenv())
# # Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
# API_TOKEN: str = os.getenv("TOKEN")



# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


@dp.message(and_f(invert_f(F.from_user.id == 173901673), or_f(F.content_type.in_({ContentType.PHOTO}), Text(startswith='Привет'))))
async def send_photo_echo(message: Message):
    print("I am in send_photo_echo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(message)


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    print("I am in send_echo")
    print("message =  ", message)
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')


if __name__ == '__main__':
    print("Bot is polling")
    dp.run_polling(bot)
