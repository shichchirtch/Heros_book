from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import edit_bookmarks_button, cancel
from pagination import pagin_dict
from external_functions import format_bookmark_name_button
from last_words import *

def create_bookmarks_keyboard(language:int, *args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        print('button = ', button)
        using_language = 1
        if button < 100:
            new_butt = button
            using_dict = pagin_dict
            first_name = ''
            using_language = language

        elif 200< button<300:
            new_butt = int(str(button)[2:])
            using_dict = kriger
            first_name = 'Кригер - '

        elif 300<button<400:
            new_butt = int(str(button)[2:])
            using_dict = gorinov
            first_name = 'Горинов - '

        elif 400<button<500:
            new_butt = int(str(button)[2:])
            using_dict = yashin
            first_name = 'Яшин - '

        elif 500<button<600:
            new_butt = int(str(button)[2:])
            using_dict = kara_murza
            first_name = 'Кара-Мурза - '

        elif 600<button<700:
            new_butt = int(str(button)[2:])
            using_dict = navalny
            first_name = 'Навальный - '

        elif 700<button<800:
            new_butt = int(str(button)[2:])
            using_dict = pivovarov
            first_name = 'Пивоваров - '

        elif 800<button<900:
            new_butt = int(str(button)[2:])
            using_dict = skolichenko
            first_name = 'Сколиченко - '

        elif 900 < button < 1000:
            new_butt = int(str(button)[2:])
            using_dict = moskalev
            first_name = 'Москалёв - '

        elif 1000 < button < 1100:
            new_butt = int(str(button)[2:])
            using_dict = simonov
            first_name = 'Симонов - '

        elif 1100 < button < 1200:
            new_butt = int(str(button)[2:])
            using_dict = ivanov
            first_name = 'Иванов - '

        elif 1200 < button < 1300:
            new_butt = int(str(button)[2:])
            using_dict = afanasyev
            first_name = 'Афанасьев - '
        elif 1300 < button < 1400:
            new_butt = int(str(button)[2:])
            using_dict = gutnikova
            first_name = 'Гутникова - '

        elif 1400 < button < 1500:
            new_butt = int(str(button)[2:])
            using_dict = uvarov
            first_name = 'Уваров - '
        elif 1500 < button < 1600:
            new_butt = int(str(button)[2:])
            using_dict = kamardin
            first_name = 'Камардин - '

        elif 1600 < button < 1700:
            new_butt = int(str(button)[2:])
            using_dict = petrova
            first_name = 'Петрова - '

        elif 1700 < button < 1800:
            new_butt = int(str(button)[2:])
            using_dict = orlov
            first_name = 'Орлов - '

        elif 1800 < button < 1900:
            new_butt = int(str(button)[2:])
            using_dict = chanysheva
            first_name = 'Чанышева - '

        elif 1900 < button < 2000:
            new_butt = int(str(button)[2:])
            using_dict = galyamina
            first_name = 'Галямина - '

        elif 2000 < button < 2100:
            new_butt = int(str(button)[2:])
            using_dict = baryshnikov
            first_name = 'Барышников - '

        elif 2100 < button < 2200:
            new_butt = int(str(button)[2:])
            using_dict = ponomarenko
            first_name = 'Пономареноко - '

        actual_string = format_bookmark_name_button(using_dict, button, using_language)
        kb_builder.row(InlineKeyboardButton(
            text=f'{new_butt} - {first_name}{actual_string}',  # {pagin_dict[button][1][:100]}',
            callback_data=str(button)
        ))
    # Добавляем в клавиатуру в конце две кнопки "Редактировать" и "Отменить"
    kb_builder.row(
        InlineKeyboardButton(
            text=edit_bookmarks_button[language],
            callback_data='edit_bookmarks'
        ),
        InlineKeyboardButton(
            text=cancel[language],
            callback_data='cancel'
        ),
        width=2)
    return kb_builder.as_markup()




def create_edit_keyboard(language:int, *args: int) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    for button in sorted(args):
        print('button = ', button)
        using_language = 1
        if button<100:
            new_butt = button
            using_dict = pagin_dict
            using_language = language

        elif 200<button<300:
            new_butt = int(str(button)[2:])
            using_dict = kriger

        elif 300<button<400:
            new_butt = int(str(button)[2:])
            using_dict = gorinov
        elif 400<button<500:
            new_butt = int(str(button)[2:])
            using_dict = yashin

        elif 500<button<600:
            new_butt = int(str(button)[2:])
            using_dict = kara_murza

        elif 600<button<700:
            new_butt = int(str(button)[2:])
            using_dict = navalny

        elif 700<button<800:
            new_butt = int(str(button)[2:])
            using_dict = pivovarov

        elif 800<button<900:
            new_butt = int(str(button)[2:])
            using_dict = skolichenko

        elif 900 < button < 1000:
            new_butt = int(str(button)[2:])
            using_dict = skolichenko

        elif 1000 < button < 1100:
            new_butt = int(str(button)[2:])
            using_dict = simonov

        elif 1100 < button < 1200:
            new_butt = int(str(button)[2:])
            using_dict = ivanov

        elif 1200 < button < 1300:
            new_butt = int(str(button)[2:])
            using_dict = afanasyev

        elif 1300 < button < 1400:
            new_butt = int(str(button)[2:])
            using_dict = gutnikova

        elif 1400 < button < 1500:
            new_butt = int(str(button)[2:])
            using_dict = uvarov

        elif 1500 < button < 1600:
            new_butt = int(str(button)[2:])
            using_dict = kamardin

        elif 1600 < button < 1700:
            new_butt = int(str(button)[2:])
            using_dict = petrova

        elif 1700 < button < 1800:
            new_butt = int(str(button)[2:])
            using_dict = orlov

        elif 1800 < button < 1900:
            new_butt = int(str(button)[2:])
            using_dict = chanysheva
        elif 1900 < button < 2000:
            new_butt = int(str(button)[2:])
            using_dict = galyamina
        elif 2000 < button < 2100:
            new_butt = int(str(button)[2:])
            using_dict = baryshnikov
        elif 2100 < button < 2200:
            new_butt = int(str(button)[2:])
            using_dict = ponomarenko
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания

        kb_builder.row(InlineKeyboardButton(
            text=f'❌ {new_butt} - {format_bookmark_name_button(using_dict, button, using_language)}',
            callback_data=f'{button}del'
        ))
    # Добавляем в конец клавиатуры кнопку "Отменить"
    kb_builder.row(
        InlineKeyboardButton(
            text=cancel[language],
            callback_data='cancel'
        )
    )
    return kb_builder.as_markup()