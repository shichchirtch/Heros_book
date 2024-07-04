from aiogram import F, Router
from filters import *
from lexicon import language_kit, last_words_russian_only
import asyncio
from pagination import pagin_dict
from aiogram.types import CallbackQuery, Message, InputMediaPhoto
from aiogram.exceptions import TelegramBadRequest
from inline_keyboard import create_pagination_keyboard
from bookmark_kb import create_edit_keyboard
from lexicon import (other_ant, dlina_doc, bookmark_10,
                     bookmark_add, bookmark_list,
                     no_bookmarks, edit_bookmarks)
from postgres_functions import (return_current_page_index,
                                page_listai,
                                return_langauge_index,
                                return_bookmark_list,
                                add_new_bookmarks,
                                set_new_page,
                                return_modified_pagina_list,
                                return_reserv_nod_from_base,
                                add_reserved_msg,
                                return_last_nod_from_modified_pagina,
                                insert_new_page_in_modified_pagina,
                                del_bookmarck)
from bot_instance import bot
import json
from aiogram.fsm.context import FSMContext
from last_words import *
from FSM import FSM_NAMES
from copy import deepcopy

lese_router = Router()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед-назад"
# во время взаимодействия пользователя с сообщением-книгой
@lese_router.callback_query(MOVE_PAGE())
async def page_moving(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    bot_state = await state.get_state()
    print('bot_state = ', bot_state, 'type = ', type(bot_state))
    dict_key = bot_state.split(':')[1]
    dict_collection['base_part'] = pagin_dict
    using_dict = dict_collection[dict_key]
    shift = -1 if callback.data == 'backward' else 1
    await page_listai(user_id, shift)
    pagin_index = await return_current_page_index(user_id)
    language = await  return_langauge_index(user_id)
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=using_dict[pagin_index][0], caption=using_dict[pagin_index][language]),
            reply_markup=create_pagination_keyboard(using_dict, pagin_index)
        )
    except TelegramBadRequest:
        print('////Into Exeption Page Moving')
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=pagin_dict[1][0], caption=pagin_dict[1][language]),
            reply_markup=create_pagination_keyboard(using_dict, pagin_index))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с номером текущей страницы и добавлять текущую страницу в закладки
@lese_router.callback_query(lambda x: '/' in x.data and x.data.replace(' / ', '').isdigit())
async def process_page_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    language = await return_langauge_index(user_id)
    bookmark_list = await return_bookmark_list(user_id)
    current_page_index = await return_current_page_index(user_id)
    if len(bookmark_list) < 11 and current_page_index not in bookmark_list:
        await add_new_bookmarks(user_id, current_page_index)
        print('**********')
        await callback.answer(bookmark_add[language])
    else:
        att = await callback.message.answer(bookmark_10[language])
        await asyncio.sleep(3)
        await att.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с закладкой из списка закладок
@lese_router.callback_query(IS_DIGIT_CALLBACK_DATA())
async def process_bookmark_press(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    print('callbackdata = ', callback.data, type(callback.data))
    await set_new_page(user_id, int(callback.data))
    current_index = await return_current_page_index(user_id)
    list_user_msg = await return_modified_pagina_list(user_id)
    if len(list_user_msg) == 0:
        reserved_msg = await return_reserv_nod_from_base(user_id)
        reserved_copi = deepcopy(reserved_msg)
        await add_reserved_msg(user_id, reserved_copi)

    last_message = await return_last_nod_from_modified_pagina(user_id)
    return_to_message = Message(**json.loads(last_message))
    print('type return_to_message = ', type(return_to_message), '\n\n', return_to_message)
    msg = Message.model_validate(return_to_message).as_(bot)
    if int(callback.data) < 100:
        using_dict = pagin_dict
        await state.set_state(FSM_NAMES.base_part)
    else:
        digit_key = int(callback.data) // 100
        using_dict = dict_digit_collection[digit_key]
        if digit_key == 2:
            await state.set_state(FSM_NAMES.kriger)
        elif digit_key == 3:
            await state.set_state(FSM_NAMES.gorinov)
        elif digit_key == 4:
            await state.set_state(FSM_NAMES.kara_murza)
        elif digit_key == 5:
            await state.set_state(FSM_NAMES.yashin)
        elif digit_key == 6:
            await state.set_state(FSM_NAMES.navalny)
        elif digit_key == 7:
            await state.set_state(FSM_NAMES.pivovarov)
        elif digit_key == 8:
            await state.set_state(FSM_NAMES.skolichenko)
        elif digit_key == 9:
            await state.set_state(FSM_NAMES.moskalev)
        elif digit_key == 10:
            await state.set_state(FSM_NAMES.simonov)
        elif digit_key == 11:
            await state.set_state(FSM_NAMES.ivanov)
        elif digit_key == 12:
            await state.set_state(FSM_NAMES.afanasyev)
        elif digit_key == 13:
            await state.set_state(FSM_NAMES.gutnikova)
        elif digit_key == 14:
            await state.set_state(FSM_NAMES.uvarov)
        elif digit_key == 15:
            await state.set_state(FSM_NAMES.kamardin)
        elif digit_key == 16:
            await state.set_state(FSM_NAMES.petrova)
        elif digit_key == 17:
            await state.set_state(FSM_NAMES.orlov)
        elif digit_key == 18:
            await state.set_state(FSM_NAMES.chanysheva)
        elif digit_key == 19:
            await state.set_state(FSM_NAMES.galyamina)
        elif digit_key == 20:
            await state.set_state(FSM_NAMES.baryshnikov)
        elif digit_key == 21:
            await state.set_state(FSM_NAMES.ponomarenko)

    try:
        att = await msg.edit_media(
            media=InputMediaPhoto(
                media=using_dict[current_index][0], caption=using_dict[current_index][1]),
            reply_markup=create_pagination_keyboard(using_dict, current_index))
        str_att = att.model_dump_json(exclude_none=True)
        await insert_new_page_in_modified_pagina(user_id, str_att)
    except TelegramBadRequest:
        print('Into Exeption in process_bookmark_press')
        await insert_new_page_in_modified_pagina(user_id, last_message)
    await callback.message.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "редактировать" под списком закладок
@lese_router.callback_query(F.data == 'edit_bookmarks')
async def process_edit_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    language = await return_langauge_index(user_id)
    bookmarks = await return_bookmark_list(user_id)
    await callback.message.edit_text(
        text=edit_bookmarks[language],
        reply_markup=create_edit_keyboard(language,   *bookmarks))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "отменить" во время работы со списком закладок (просмотр и редактирование)
@lese_router.callback_query(F.data == 'cancel')
async def process_cancel_press(callback: CallbackQuery):
    print('process_cancel_press works ')
    await callback.message.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с закладкой из списка закладок к удалению
@lese_router.callback_query(IS_DEL_BUCKMARK())
async def process_del_bookmark_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    language = await return_langauge_index(user_id)
    del_page_index = int(callback.data[:-3])
    print('callback.data[:-3] = ', callback.data[:-3])
    #  Интересно поглядеть, как это реализоваtb в Постгрессе
    await del_bookmarck(user_id, del_page_index)
    bookmarks = await return_bookmark_list(user_id)

    if await return_bookmark_list(user_id):
        await (
            callback.message.edit_text(
                text=bookmark_list[language],
                reply_markup=create_edit_keyboard(language,    *bookmarks)))
    else:
        no_marks_respond = await callback.message.edit_text(text=no_bookmarks[language])
        print('no_marks_respond = ')
        await asyncio.sleep(2)
        await no_marks_respond.delete()
    await callback.answer()


@lese_router.message()
async def send_echo(message: Message, state: FSMContext):
    print("Works send_echo")
    bot_state = await state.get_state()
    state_name = bot_state.split(":")[1]
    using_dict = dict_collection[state_name]
    dlina = len(using_dict)
    language = await return_langauge_index(message.from_user.id)
    if message.text.isdigit():
        antwort = await message.reply(f'{dlina_doc[language]} - {dlina}')
        await asyncio.sleep(2)
        await message.delete()
        await asyncio.sleep(1)
        await antwort.delete()
    elif message.text in language_kit:
        if message.text in ('eng', 'en', 'енг', 'an', 'утп', '/eng', '/en', 'анг'):
            language = 2
        elif message.text in ('de' 'ву', '/de', 'нем', 'ge'):
            language = 3
        att = await message.answer(last_words_russian_only[language])
        await asyncio.sleep(3)
        await message.delete()
        await asyncio.sleep(5)
        await att.delete()
    else:
        antwort = await message.reply(other_ant[language])
        await asyncio.sleep(3)
        await message.delete()
        await antwort.delete()
