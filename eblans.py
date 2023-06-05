#  ______     ______     ______     ______     ______   __     ______     ______
# /\  ___\   /\  == \   /\  ___\   /\  __ \   /\__  _\ /\ \   /\___  \   /\  ___\
# \ \ \____  \ \  __<   \ \  __\   \ \  __ \  \/_/\ \/ \ \ \  \/_/  /__  \ \  __\
#  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\    \ \_\  \ \_\   /\_____\  \ \_____\
#   \/_____/   \/_/ /_/   \/_____/   \/_/\/_/     \/_/   \/_/   \/_____/   \/_____/

# Code is licensed under CC-BY-NC-ND 4.0 unless otherwise specified.
# https://creativecommons.org/licenses/by-nc-nd/4.0/
# You CANNOT edit this file without direct permission from the author.
# You can redistribute this file without any changes.

import asyncio

from aiogram import Bot, exceptions

BOT_TOKEN = ""
CHAT_ID = -100
EBLANS_FILE = "eblans.txt"

bot = Bot(token=BOT_TOKEN)


async def read_eblans_count():
    try:
        with open(EBLANS_FILE, "r") as file:
            eblans_count = int(file.read())
    except FileNotFoundError:
        eblans_count = 1
    return eblans_count


async def write_eblans_count(eblans_count):
    with open(EBLANS_FILE, "w") as file:
        file.write(str(eblans_count))


def format_eblans_message(eblans_count):
    if eblans_count % 1000 == 0:
        return f"{eblans_count} fucking eblans."
    else:
        endings = ("ов", "", "а")
        index = (
            1
            if eblans_count % 10 == 1 and eblans_count % 100 != 11
            else (
                2
                if eblans_count % 10 >= 2
                and eblans_count % 10 <= 4
                and (eblans_count % 100 < 10 or eblans_count % 100 >= 20)
                else 0
            )
        )
        return f"{eblans_count} еблан{endings[index]}."


async def send_message_to_chat():
    eblans_count = await read_eblans_count()
    message_text = format_eblans_message(eblans_count + 1)

    await asyncio.sleep(2.6)

    try:
        await bot.send_message(CHAT_ID, message_text)
    except exceptions.TelegramAPIError as e:
        print(f"! Ошибка: {str(e)}")
        await asyncio.sleep(5)

    await write_eblans_count(eblans_count + 1)


async def start_sending_messages():
    while True:
        await send_message_to_chat()


async def main():
    await start_sending_messages()


if __name__ == "__main__":
    asyncio.run(main())
