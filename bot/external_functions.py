from aiogram.types import Message, InputMediaPhoto
from inline_keyboard import create_pagination_keyboard
from pagination import pagin_dict
import json
from sqlalchemy import select
from aiogram.exceptions import TelegramBadRequest
from bot_instance import bot
from lexicon import help_command, contacts
from bs4 import BeautifulSoup
# from postgres_functions import (return_langauge_index,
#                                 return_current_page_index,
#                                 return_modified_pagina_list,
#                                 return_reserv_nod_from_base,
#                                 insert_new_page_in_modified_pagina,
#                                 return_last_nod_from_modified_pagina)
from bot_base import session_marker, User
from copy import deepcopy


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
        user_messege_list =needed_data.modified_pagina  #users_db[user_id]['reading process']

        if len(user_messege_list) == 0:
            print('We are into deep ERROR !')
            reserve_msg = needed_data.reserved_first_message #users_db[user_id]['reserved_first_message']
            reserve_nod_copy = deepcopy(reserve_msg)
            needed_data.modified_pagina = [reserve_nod_copy]
            user_messege_list = needed_data.modified_pagina

        last_message = user_messege_list.pop() # users_db[user_id]['reading process'].pop()
        print('type last_message = ', type(last_message))
        return_to_message = Message(**json.loads(last_message))
        print('type return_to_message = ', type(return_to_message))
        msg = Message.model_validate(return_to_message).as_(bot)
        # print('msg = ', msg)
        try:
            att = await msg.edit_media(
                media=InputMediaPhoto(
                    media=pagin_dict[current_page][0], caption=pagin_dict[current_page][language]),
                reply_markup=create_pagination_keyboard(pagin_dict, current_page))
            str_att = att.model_dump_json(exclude_none=True)
            updated_user_list = user_messege_list+[str_att]  # users_db[user_id]['reading process'].append(str_att)
            needed_data.modified_pagina = updated_user_list
            # await session.commit()

        except TelegramBadRequest:
            print('Into Exeption*****')
            await msg.delete()
            att_exc = await message.answer_photo(
                photo=pagin_dict[current_page][0],
                caption=pagin_dict[current_page][language],
                reply_markup=create_pagination_keyboard(current_page))
            json_att = att_exc.model_dump_json(exclude_none=True)
            updated_user_list = user_messege_list + [json_att]
            needed_data.modified_pagina = updated_user_list
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
        user_messege_list = needed_data.modified_pagina  # users_db[user_id]['reading process']

        if len(user_messege_list) == 0:
            print('We are into deep ERROR in HELP !')
            reserve_msg = needed_data.reserved_first_message  # users_db[user_id]['reserved_first_message']
            reserve_nod_copy = deepcopy(reserve_msg)
            needed_data.modified_pagina = [reserve_nod_copy]
            user_messege_list = needed_data.modified_pagina

        last_message = user_messege_list.pop()
        return_to_message = Message(**json.loads(last_message))
        msg = Message.model_validate(return_to_message).as_(bot)
        # print('msg = ', msg)
        if message.text == '/help':
            using_ant = help_command
        else:
            using_ant = contacts
        try:
            att = await msg.edit_media(
                media=InputMediaPhoto(
                    media=using_ant[0], caption=using_ant[language]),
                reply_markup=None)
            str_att = att.model_dump_json(exclude_none=True)
            print(str_att)
            updated_user_list = user_messege_list + [str_att]
            needed_data.modified_pagina = updated_user_list
            # await session.commit()

        except TelegramBadRequest:
            print('Into help Exeption*****')
            await msg.delete()
            att_exc = await message.answer_photo(
                photo=using_ant[0],
                caption=using_ant[language],
                reply_markup=None)
            json_att = att_exc.model_dump_json(exclude_none=True)
            updated_user_list = user_messege_list + [json_att]  # users_db[user_id]['reading process'].append(str_att)
            needed_data.modified_pagina = updated_user_list
        await session.commit()
            # users_db[message.from_user.id]['reading process'].append(json_att)


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
        user_messege_list = needed_data.modified_pagina  # users_db[user_id]['reading process']

        if len(user_messege_list) == 0:
            print('We are into deep ERROR Last word !')
            reserve_msg = needed_data.reserved_first_message
            reserve_nod_copy = deepcopy(reserve_msg)
            needed_data.modified_pagina = [reserve_nod_copy]
            user_messege_list = needed_data.modified_pagina

        last_message = user_messege_list.pop()
        print('type last_message = ', type(last_message))
        return_to_message = Message(**json.loads(last_message))
        print('type return_to_message = ', type(return_to_message))
        msg = Message.model_validate(return_to_message).as_(bot)
    try:
        att = await msg.edit_media(
            media=InputMediaPhoto(
                media=last_word_dict[current_page][0], caption=last_word_dict[current_page][1]),
            reply_markup=create_pagination_keyboard(last_word_dict, current_page))

        str_att = att.model_dump_json(exclude_none=True)
        updated_user_list = user_messege_list + [str_att]  # users_db[user_id]['reading process'].append(str_att)
        needed_data.modified_pagina = updated_user_list

    except TelegramBadRequest:
        print('Into Last Word Exeption *****')
        await msg.delete()
        att_exc = await message.answer_photo(
            photo=pagin_dict[current_page][0],
            caption=pagin_dict[current_page][1],
            reply_markup=create_pagination_keyboard(current_page))

        json_att = att_exc.model_dump_json(exclude_none=True)
        updated_user_list = user_messege_list + [json_att]
        needed_data.modified_pagina = updated_user_list
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



    # async with session_marker() as session:
    #     query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
    #     needed_data = query.scalar()
    #     print('works change_language')
    #     if language in ('rus', 'кгы'):
    #         needed_data.language = 0
    #     elif language in ('eng', 'утп'):
    #         needed_data.language = 1
    #     else:
    #         needed_data.language = 2
    #     await session.commit()
