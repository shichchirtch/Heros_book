from aiogram import Router, F, html
import asyncio
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command, StateFilter
from external_functions import (edit_repeat_text_window,
                                change_language, edit_help_window,
                                edit_last_word_window)

from postgres_functions import (insert_new_user_in_table,
                                check_user_in_table,
                                insert_new_page_in_modified_pagina,
                                insert_page_in_reserved_first_message,
                                go_back_to_beginning,
                                go_to_faces,
                                set_new_page,
                                return_bookmark_list)

from inline_keyboard import create_pagination_keyboard
from bookmark_kb import create_bookmarks_keyboard
from filters import CHECK_NUMBER, PRE_START
from pagination import pagin_dict
from start_menu import pre_start_clava
from copy import deepcopy
from lexicon import *
from aiogram.fsm.context import FSMContext
from FSM import FSM_NAMES
from last_words import *
from postgres_functions import return_langauge_index

ch_router = Router()


@ch_router.message(~F.text)
async def delete_not_text_type_messages(message: Message):
    await message.delete()


@ch_router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    user_name = message.from_user.first_name
    user_tg_id = message.from_user.id
    if not await check_user_in_table(user_tg_id):
        await insert_new_user_in_table(user_tg_id, user_name)
        await state.set_state(FSM_NAMES.base_part)

        first_antwort = await message.answer(
            text=f'<b>{html.bold(html.quote(user_name))}</b>, сейчас Вы узнаете много интересного !',
            parse_mode=ParseMode.HTML,
            reply_markup=ReplyKeyboardRemove())

        att = await message.answer_photo(
            photo=pagin_dict[1][0],
            caption=pagin_dict[1][1],
            reply_markup=create_pagination_keyboard())

        str_start_page = att.model_dump_json(exclude_none=True)
        copy_start_page = deepcopy(str_start_page)
        await insert_new_page_in_modified_pagina(user_tg_id, str_start_page)
        await insert_page_in_reserved_first_message(user_tg_id, copy_start_page)
        await asyncio.sleep(4)
        await first_antwort.delete()

    await message.delete()


@ch_router.message(PRE_START())
async def before_start(message: Message):
    prestart_ant = await message.answer(text='Нажми на кнопку <b>start</b> !',
                                        reply_markup=pre_start_clava)
    await message.delete()
    await asyncio.sleep(4)
    await prestart_ant.delete()


@ch_router.message(Command(commands='help'), ~StateFilter(FSM_NAMES.waiting))
async def process_help_command(message: Message):
    print('help works')
    await edit_help_window(message)  # First usage
    await message.delete()


@ch_router.message(Command(commands='otzyv'), ~StateFilter(FSM_NAMES.waiting))
async def process_command_otzyv(message: Message, state: FSMContext):
    print("**************************************")
    language = await return_langauge_index(message.from_user.id)
    await state.set_state(FSM_NAMES.otzyv)
    att = await message.answer(text_for_send_refferal[language])
    await message.delete()
    await asyncio.sleep(15)
    await att.delete()


@ch_router.message(StateFilter(FSM_NAMES.otzyv))
async def process_send_otzyv(message: Message, state: FSMContext):
    print('feed_back sending\n ')
    user_id = message.from_user.id
    await state.set_state(FSM_NAMES.waiting)
    language = await return_langauge_index(user_id)
    sending_data = message.text
    user_name = message.from_user.first_name
    join_text = f'User_id {user_id}, user_name  {user_name} \n\nsend MESSAGE \n\n{sending_data}'
    await message.bot.send_message(chat_id=-4241930933, text=join_text)
    await asyncio.sleep(1)
    await message.delete()
    att = await message.answer(success_send[language])
    await asyncio.sleep(3)
    await att.delete()
    wait_att = await message.answer(waiting_15[language])
    await asyncio.sleep(3)
    await  asyncio.sleep(90)
    await wait_att.delete()
    await state.set_state(FSM_NAMES.base_part)


@ch_router.message(StateFilter(FSM_NAMES.waiting))
async def process_waiting(message: Message):
    print('waiting please\n ')
    language = await return_langauge_index(message.from_user.id)
    att = await message.answer(just_waitng[language])
    await asyncio.sleep(3)
    await message.delete()
    await att.delete()


@ch_router.message(Command(commands='contacts'))
async def process_contact_command(message: Message):
    print('contact works')

    await edit_help_window(message)
    await message.delete()


@ch_router.message(F.text.lower().in_(language_kit), StateFilter(FSM_NAMES.base_part))
async def set_language(message: Message):
    print('смена языка')
    user_tg_id = message.from_user.id
    lang = message.text.lower()
    if lang in ('rus', 'кгы', '/rus', 'рус', 'рус'):
        digit_language_identifikator = 1
    elif lang in ( 'eng', 'en', 'енг', 'an',  'утп' '/eng', '/en', 'анг'):
        digit_language_identifikator = 2
    else:
        digit_language_identifikator = 3
    current_languge = await return_langauge_index(user_tg_id)
    if current_languge != digit_language_identifikator:
        await change_language(user_tg_id, lang)
        language = await return_langauge_index(message.from_user.id)  # await get_user_language(user_tg_id)
        att = await message.answer(text=language_responce[language],
                                   reply_markup=ReplyKeyboardRemove())
        await edit_repeat_text_window(message)
        await message.delete()
        await asyncio.sleep(3)
        await att.delete()
    else:
        await asyncio.sleep(1)
        await message.delete()


@ch_router.message(Command(commands='about_project'))
async def process_beginning_command(message: Message, state: FSMContext):
    print('ABOUT PROJECT works')
    await state.set_state(FSM_NAMES.base_part)
    await go_back_to_beginning(message.from_user.id)
    await edit_repeat_text_window(message)
    await message.delete()


@ch_router.message(Command(commands='faces'))
async def process_faces_command(message: Message, state: FSMContext):
    print('faces works')
    await state.set_state(FSM_NAMES.base_part)
    await go_to_faces(message.from_user.id)
    await edit_repeat_text_window(message)
    await message.delete()


@ch_router.message(Command(commands='continue'))
async def process_continue_command(message: Message):
    language = await return_langauge_index(message.from_user.id)
    cont_ant = await message.answer(continue_ans[language])
    await message.delete()
    await asyncio.sleep(1)
    await cont_ant.delete()


@ch_router.message(~StateFilter(FSM_NAMES.otzyv), CHECK_NUMBER())
async def set_page_number(message: Message, state: FSMContext):
    print('set_page works\n')
    bot_state = await state.get_state()
    user_id = message.from_user.id
    key_for_pagin = bot_state.split(':')[1]
    head_index_FSM = pagin_collection[key_for_pagin]
    if message.text.startswith('/'):
        message_page = int(message.text[1:])  # await set_new_pag
    else:
        message_page = int(message.text)
    summa_two_page_indexes = head_index_FSM + message_page
    await set_new_page(user_id, summa_two_page_indexes)

    if bot_state == 'FSM_NAMES:base_part':
        await edit_repeat_text_window(message)
    else:
        dict_key = bot_state.split(':')[1]
        passing_dict = dict_collection[dict_key]
        await edit_last_word_window(bot_state, passing_dict, message)
    await message.delete()


# Этот хэндлер будет срабатывать на команду "/bookmarks"
# и отправлять пользователю список сохраненных закладок,
# если они есть или сообщение о том, что закладок нет
@ch_router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message):
    print('process_bookmarks_command works')
    user_id = message.from_user.id
    language = await return_langauge_index(user_id)
    bookmarks = await return_bookmark_list(user_id)
    if bookmarks:
        await message.answer(
            text=bookmark_list[language],
            reply_markup=create_bookmarks_keyboard(language,
                                                   *bookmarks))
    else:
        no_bookmark = await message.answer(text=no_bookmarks[language])
        await asyncio.sleep(4)
        await no_bookmark.delete()
    await message.delete()


@ch_router.message(Command(commands='exit'))
async def process_command_exit(message: Message, state: FSMContext):
    print('exit works\n ')
    await state.set_state(FSM_NAMES.base_part)
    await go_to_faces(message.from_user.id)
    await edit_repeat_text_window(message)  # 4 usage
    await message.delete()


@ch_router.message(Command(commands='Kriger'))
async def process_kriger_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.kriger)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, kriger, message)
    await message.delete()


@ch_router.message(Command(commands='Gorinov'))
async def process_gorinov_command_state(message: Message, state: FSMContext):
    print('gorinov works\n message = ')
    await state.set_state(FSM_NAMES.gorinov)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, gorinov, message)
    await message.delete()


@ch_router.message(Command(commands='Yashin'))
async def process_yashin_command_state(message: Message, state: FSMContext):
    print('Yashin works')
    await state.set_state(FSM_NAMES.yashin)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, yashin, message)
    await message.delete()


@ch_router.message(Command(commands='KaraMurza'))
async def process_karamurza_command_state(message: Message, state: FSMContext):
    print('KM works')
    await state.set_state(FSM_NAMES.kara_murza)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, kara_murza, message)
    await message.delete()


@ch_router.message(Command(commands='Navalny'))
async def process_navalny_command_state(message: Message, state: FSMContext):
    print('KM works')
    await state.set_state(FSM_NAMES.navalny)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, navalny, message)
    await message.delete()


@ch_router.message(Command(commands='Pivovarov'))
async def process_pivovarov_command_state(message: Message, state: FSMContext):
    print('KM works')
    await state.set_state(FSM_NAMES.pivovarov)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, pivovarov, message)
    await message.delete()


@ch_router.message(Command(commands='Skolichenko'))
async def process_skol_command_state(message: Message, state: FSMContext):
    print('Skol works')
    await state.set_state(FSM_NAMES.skolichenko)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, skolichenko, message)
    await message.delete()


@ch_router.message(Command(commands='Moskalev'))
async def process_moskalev_command_state(message: Message, state: FSMContext):
    print('Moskalev works')
    await state.set_state(FSM_NAMES.moskalev)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, moskalev, message)
    await message.delete()


@ch_router.message(Command(commands='Simonov'))
async def process_simonov_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.simonov)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, simonov, message)
    await message.delete()


@ch_router.message(Command(commands='Ivanov'))
async def process_ivanov_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.ivanov)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, ivanov, message)
    await message.delete()


@ch_router.message(Command(commands='Afanasyev'))
async def process_afanasyev_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.afanasyev)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, afanasyev, message)
    await message.delete()


@ch_router.message(Command(commands='Gutnikova'))
async def process_gutnikova_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.gutnikova)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, gutnikova, message)
    await message.delete()


@ch_router.message(Command(commands='Uvarov'))
async def process_uvarov_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.uvarov)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, uvarov, message)
    await message.delete()


@ch_router.message(Command(commands='Kamardin'))
async def process_kamardin_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.kamardin)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, kamardin, message)
    await message.delete()


@ch_router.message(Command(commands='Petrova'))
async def process_petrova_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.petrova)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, petrova, message)
    await message.delete()


@ch_router.message(Command(commands='Orlov'))
async def process_orlov_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.orlov)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, orlov, message)
    await message.delete()


@ch_router.message(Command(commands='Chanysheva'))
async def process_chanysheva_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.chanysheva)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, chanysheva, message)
    await message.delete()


@ch_router.message(Command(commands='Galyamina'))
async def process_galyamina_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.galyamina)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, galyamina, message)
    await message.delete()


@ch_router.message(Command(commands='Baryshnikov'))
async def process_baryshnikov_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.baryshnikov)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, baryshnikov, message)
    await message.delete()


@ch_router.message(Command(commands='Ponomarenko'))
async def process_ponomarenko_command_state(message: Message, state: FSMContext):
    await state.set_state(FSM_NAMES.ponomarenko)
    current_state = await state.get_state()
    await edit_last_word_window(current_state, ponomarenko, message)
    await message.delete()
