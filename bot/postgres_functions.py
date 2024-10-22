from bot_base import session_marker, User
from sqlalchemy import select, func
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from lexicon import users_db
from aiogram.types import CallbackQuery, Message
async def insert_new_user_in_table(user_tg_id: int, name: str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        if not needed_data:
            print('Now we are into first function')
            new_us = User(tg_us_id=user_tg_id, user_name=name)
            session.add(new_us)
            await session.commit()


async def check_user_in_table(user_tg_id:int):
    """Функция проверяет есть ли юзер в БД"""
    async with session_marker() as session:
        print("Work check_user Function")
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        data = query.one_or_none()
        return data

async def insert_new_page_in_modified_pagina(user_tg_id: int, new_page:str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        print('insert_first_page_in_modified_pagina')
        needed_data.modified_pagina = new_page
        await session.commit()

async def return_langauge_index(user_tg_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        return needed_data.language

async def return_current_page_index(user_tg_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        return needed_data.page


async def return_modified_pagina(user_id):
    async with session_marker() as session:
        print("Works return_last_nod_from_modified_pagina Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        pagina = needed_data.modified_pagina
        return pagina

async def go_back_to_beginning(user_tg_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        print('\ngo_back_to_beginning')
        needed_data.page = 1
        await session.commit()

async def go_to_faces(user_tg_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        print('\ngo_to faces')
        needed_data.page = 6
        await session.commit()

async def set_new_page(user_tg_id:int, index_new_page:int):
    """Функия перелистывает страницу на запрашиваемую"""
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        print('\nset_new_page')
        needed_data.page = index_new_page
        await session.commit()

async def return_bookmark_list(user_id):
    async with session_marker() as session:
        print("Works return_len_bookmark_list Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        bookmark_list = needed_data.bookmarks
        return bookmark_list

async def page_listai(user_id:int, schift:int):
    async with session_marker() as session:
        print("Work page_moving Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        print('data = ', needed_data)
        needed_data.page +=schift
        await session.commit()


async def add_new_bookmarks(user_tg_id: int, adding_page:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        print('add_new_bookmarks works')
        bookmark_list = needed_data.bookmarks
        new_list = bookmark_list+[adding_page]
        needed_data.bookmarks = new_list
        await session.commit()


async def del_bookmarck(user_tg_id: int, delete_page:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        print('del_bookmarks works')
        bookmark_list = needed_data.bookmarks
        temp_arr = []
        for x in bookmark_list:
            if x != delete_page:
                temp_arr.append(x)
        needed_data.bookmarks = temp_arr
        await session.commit()


async def message_trasher(user_id:int, msg:Message|None|CallbackQuery):
    if msg:
        with suppress(TelegramBadRequest):
            await msg.delete()
            users_db[user_id]['bot_ans'] = ''
    else:
        pass


async def get_user_count():
    async with session_marker() as session:
        result = await session.execute(select(func.count(User.index)))
        count = result.scalar()
        return count
