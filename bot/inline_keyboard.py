from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pagination import pagin_dict
from last_words import *


def create_pagination_keyboard(using_dict=pagin_dict, page=1) -> InlineKeyboardMarkup:
    if page > 99:
        slice_page = int(str(page)[-2:])
        page = slice_page

    elif 200<page<300:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = kriger
    elif 300<page<400:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = gorinov

    elif 400<page<500:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = yashin

    elif 500<page<600:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = kara_murza

    elif 600<page<700:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = navalny

    elif 700<page<800:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = pivovarov

    elif 800<page<900:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = skolichenko

    elif 900<page<1000:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = moskalev

    elif 1000<page<1100:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = simonov

    elif 1100<page<1200:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = ivanov

    elif 1200<page<1300:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = afanasyev

    elif 1300<page<1400:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = gutnikova

    elif 1400<page<1500:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = uvarov

    elif 1500<page<1600:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = kamardin

    elif 1600<page<1700:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = petrova

    elif 1700<page<1800:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = orlov

    elif 1800<page<1900:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = chanysheva
    elif 1900<page<2000:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = galyamina

    elif 2000<page<2100:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = baryshnikov

    elif 2100<page<2200:
        slice_page = int(str(page)[-2:])
        page = slice_page
        using_dict = ponomarenko

    dlina = len(using_dict)
    forward_button = InlineKeyboardButton(text=f'>>', callback_data='forward')
    middle_button = InlineKeyboardButton(text=f'{page} / {dlina}', callback_data=f'{page} / {dlina}')
    backward_button = InlineKeyboardButton(text='<<', callback_data='backward')
    if page == 1:
        pagination_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[forward_button]]

        )
        return pagination_keyboard
    elif  1 < page < len(using_dict):
        pagination_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[backward_button, middle_button, forward_button]])
        return pagination_keyboard

    else:
        pagination_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[backward_button, middle_button]])
        return pagination_keyboard
