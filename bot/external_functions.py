from aiogram.types import Message, InputMediaPhoto
from inline_keyboard import create_pagination_keyboard
from pagination import pagin_dict
import json
from sqlalchemy import select
from aiogram.exceptions import TelegramBadRequest
from bot_instance import bot
from lexicon import help_command, contacts
from bs4 import BeautifulSoup
from postgres_functions import (return_langauge_index,
                                return_current_page_index,
                                insert_new_page_in_modified_pagina,
                                )
from bot_base import session_marker, User
import asyncio


async def edit_repeat_text_window(message: Message):
    """Эта асинхронная функция редактирует открытую прежде страницу, если юзер нажал
    на какую нибудь кнопку создающее новое окно, а не редактирующее старое с текстом"""
    print("edit FUNC WORKS")
    user_id = message.from_user.id
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        language = needed_data.language   # users_db[user_id]['language']
        current_page = needed_data.page  #users_db[user_id]['page']
        last_message = needed_data.modified_pagina  #users_db[user_id]['reading process']
        return_to_message = Message(**json.loads(last_message))
        msg = Message.model_validate(return_to_message).as_(bot)

        try:
            att = await msg.edit_media(
                media=InputMediaPhoto(
                    media=pagin_dict[current_page][0], caption=pagin_dict[current_page][language]),
                reply_markup=create_pagination_keyboard(pagin_dict, current_page))
            str_att = att.model_dump_json(exclude_none=True)
            needed_data.modified_pagina = str_att
        except TelegramBadRequest:
            print('Into Exeption*****')
            await msg.delete()
            att_exc = await message.answer_photo(
                photo=pagin_dict[current_page][0],
                caption=pagin_dict[current_page][language],
                reply_markup=create_pagination_keyboard(pagin_dict, current_page))
            json_att = att_exc.model_dump_json(exclude_none=True)
            needed_data.modified_pagina = json_att
        await session.commit()


# except IndexError:
async def edit_help_window(message: Message):
    """Эта асинхронная функция редактирует открытую прежде страницу в страницу help"""
    print("edit HELP FUNC WORKS")
    user_id = message.from_user.id
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        language = needed_data.language
        last_message = needed_data.modified_pagina  # users_db[user_id]['reading process']
        return_to_message = Message(**json.loads(last_message))
        msg = Message.model_validate(return_to_message).as_(bot)

        if message.text == '/help':
            using_ant = help_command
        else:
            using_ant = contacts
        att = await message.answer_photo(
            photo=using_ant[0],
            caption=using_ant[language],
            reply_markup=None)
        str_att = att.model_dump_json(exclude_none=True)
        needed_data.modified_pagina = str_att
        await msg.delete()
        await session.commit()


async def continue_window(my_dict:dict, message, user_id):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        last_message = needed_data.modified_pagina
        return_to_message = Message(**json.loads(last_message))
        page_index = needed_data.page
        msg = Message.model_validate(return_to_message).as_(bot)
        att = await message.answer_photo(
            photo=my_dict[page_index][0],
            caption=my_dict[page_index][1],
            reply_markup=create_pagination_keyboard(my_dict, page_index))
        json_att = att.model_dump_json(exclude_none=True)
        needed_data.modified_pagina = json_att
        await msg.delete()
        await session.commit()


# async def exit_window(my_dict:dict, message, user_id):
#     print("continue_word_window FUNC WORKS")
#     async with session_marker() as session:
#         query = await session.execute(select(User).filter(User.tg_us_id == user_id))
#         needed_data = query.scalar()
#         last_message = needed_data.modified_pagina
#         return_to_message = Message(**json.loads(last_message))
#         msg = Message.model_validate(return_to_message).as_(bot)
#         page_index = 6
#         att = await message.answer_photo(
#             photo=my_dict[page_index][0],
#             caption=my_dict[page_index][1],
#             reply_markup=create_pagination_keyboard(my_dict, page_index))
#         json_att = att.model_dump_json(exclude_none=True)
#         needed_data.modified_pagina = json_att
#         needed_data.page = page_index
#         await msg.delete()
#         await session.commit()


async def edit_last_word_window(state: str, last_word_dict: dict, message: Message):
    """Эта асинхронная функция редактирует last_words pagination"""
    print("edit last word  FUNC WORKS")
    user_id = message.from_user.id
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        if state == 'FSM_NAMES:kriger':
            if message.text == '/Kriger':
                current_page = 201
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 200
                needed_data.page = current_page

        elif state == 'FSM_NAMES:gorinov':
            if message.text == '/Gorinov':
                current_page = 301
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 300
                needed_data.page = current_page

        elif state == 'FSM_NAMES:yashin':
            if message.text == '/Yashin':
                current_page = 401
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 400
                needed_data.page = current_page

        elif state == 'FSM_NAMES:kara_murza':
            if message.text == '/KaraMurza':
                current_page = 501
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 500
                needed_data.page = current_page

        elif state == 'FSM_NAMES:navalny':
            if message.text == '/Navalny':
                current_page = 601
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 600
                needed_data.page = current_page

        elif state == 'FSM_NAMES:pivovarov':
            if message.text == '/Pivovarov':
                current_page = 701
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 700
                needed_data.page = current_page

        elif state == 'FSM_NAMES:skolichenko':
            if message.text == '/Skolichenko':
                current_page = 801
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 800
                needed_data.page = current_page

        elif state == 'FSM_NAMES:moskalev':
            if message.text == '/Moskalev':
                current_page = 901
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 900
                needed_data.page = current_page

        elif state == 'FSM_NAMES:simonov':
            if message.text == '/Simonov':
                current_page = 1001
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 1000
                needed_data.page = current_page

        elif state == 'FSM_NAMES:ivanov':
            if message.text == '/Ivanov':
                current_page = 1101
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 1100
                needed_data.page =current_page

        elif state == 'FSM_NAMES:afanasyev':
            if message.text == '/Afanasyev':
                current_page = 1201
                needed_data.page  = current_page
            else:
                current_page = int(message.text) + 1200
                needed_data.page = current_page

        elif state == 'FSM_NAMES:gutnikova':
            if message.text == '/Gutnikova':
                current_page = 1301
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 1300
                needed_data.page = current_page

        elif state == 'FSM_NAMES:uvarov':
            if message.text == '/Uvarov':
                current_page = 1401
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 1400
                needed_data.page = current_page

        elif state == 'FSM_NAMES:kamardin':
            if message.text == '/Kamardin':
                current_page = 1501
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 1500
                needed_data.page = current_page

        elif state == 'FSM_NAMES:petrova':
            if message.text == '/Petrova':
                current_page = 1601
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 1600
                needed_data.page = current_page

        elif state == 'FSM_NAMES:orlov':
            if message.text == '/Orlov':
                current_page = 1701
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 1700
                needed_data.page = current_page

        elif state == 'FSM_NAMES:chanysheva':
            if message.text == '/Chanysheva':
                current_page = 1801
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 1800
                needed_data.page = current_page

        elif state == 'FSM_NAMES:galyamina':
            if message.text == '/Galyamina':
                current_page = 1901
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 1900
                needed_data.page = current_page

        elif state == 'FSM_NAMES:baryshnikov':
            if message.text == '/Baryshnikov':
                current_page = 2001
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 2000
                needed_data.page = current_page

        elif state == 'FSM_NAMES:ponomarenko':
            if message.text == '/Ponomarenko':
                current_page = 2101
                needed_data.page = current_page
            else:
                current_page = int(message.text) + 2100
                needed_data.page =current_page
        await session.commit()

    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()

        current_page = needed_data.page  # users_db[user_id]['page']
        last_message = needed_data.modified_pagina  # users_db[user_id]['reading process']
        return_to_message = Message(**json.loads(last_message))
        msg = Message.model_validate(return_to_message).as_(bot)
    try:
        att = await msg.edit_media(
            media=InputMediaPhoto(
                media=last_word_dict[current_page][0], caption=last_word_dict[current_page][1]),
            reply_markup=create_pagination_keyboard(last_word_dict, current_page))

        str_att = att.model_dump_json(exclude_none=True)
        needed_data.modified_pagina = str_att

    except TelegramBadRequest:
        print('Into Last Word Exeption *****')
        await msg.delete()
        att_exc = await message.answer_photo(
            photo=pagin_dict[current_page][0],
            caption=pagin_dict[current_page][1],
            reply_markup=create_pagination_keyboard(current_page))

        json_att = att_exc.model_dump_json(exclude_none=True)
        needed_data.modified_pagina = json_att
    await session.commit()


def format_bookmark_name_button(pag_dict: dict, page_index: int, language: int) -> str:
    print('format works')
    page = pag_dict[page_index][language]
    soup = BeautifulSoup(page[:50], features="html.parser")
    s = ''
    for x in soup.get_text():
        if x != '\n':
            s += x
        else:
            s += '  '
    return s


async def change_language(user_tg_id: int, language):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        if language in ('rus', 'кгы', '/rus', 'rus', 'рус'):
            needed_data.language = 1
        elif language in ('eng', 'утп', '/eng', 'анг', 'en', '/en', 'енг', 'an'):
            needed_data.language = 2
        else:
            needed_data.language = 3
        await session.commit()

