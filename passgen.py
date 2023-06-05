#  ______     ______     ______     ______     ______   __     ______     ______
# /\  ___\   /\  == \   /\  ___\   /\  __ \   /\__  _\ /\ \   /\___  \   /\  ___\
# \ \ \____  \ \  __<   \ \  __\   \ \  __ \  \/_/\ \/ \ \ \  \/_/  /__  \ \  __\
#  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\    \ \_\  \ \_\   /\_____\  \ \_____\
#   \/_____/   \/_/ /_/   \/_____/   \/_/\/_/     \/_/   \/_/   \/_____/   \/_____/

# Code is licensed under CC-BY-NC-ND 4.0 unless otherwise specified.
# https://creativecommons.org/licenses/by-nc-nd/4.0/
# You CANNOT edit this file without direct permission from the author.
# You can redistribute this file without any changes.

import random
import string

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import bold, code

TOKEN = "YOUR-TOKEN-HERE"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def send_welcome(message: types.Message) -> None:
    """
    Sends a greeting message to the user
    """
    text = "Привет! Я бот для генерации паролей. Введите команду /psg, чтобы начать!"
    await message.reply(text=text)


@dp.message_handler(commands=["start"])
async def handle_start(message: types.Message) -> None:
    await send_welcome(message)


@dp.message_handler(commands=["psg"])
async def handle_generate_password(message: types.Message) -> None:
    """
    Generates a random password with optional length
    """
    length = int(message.get_args() or 12)
    if length < 1:
        length = 12
        response_text = f"Некорректный аргумент команды /psg. Установлена длина по умолчанию - {length}."
    else:
        password_characters = string.ascii_letters + string.digits
        password = "".join(random.choices(password_characters, k=length))
        response_text = bold("Ваш новый пароль: ") + code(password)
    await message.reply(response_text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
