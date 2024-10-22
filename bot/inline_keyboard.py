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


Kamardin_button = InlineKeyboardButton(text='Артём Камардин', url='https://telegra.ph/Artyom-Kamardin-10-19')
Mel_button = InlineKeyboardButton(text='Григорий Мельконьянц', url='https://telegra.ph/Grigorij-Melkonyanc-10-19')
Polina_button = InlineKeyboardButton(text='Полина Евтушенко', url='https://telegra.ph/Polina-Evtushenko-10-19')
Tona_button = InlineKeyboardButton(text='Антонина Фаворская', url='https://telegra.ph/Antonina-Favorskaya-10-19')
Bor_button = InlineKeyboardButton(text='Игорь Барышников', url='https://telegra.ph/Igor-Baryshnikov-10-19')
Lipzer_button = InlineKeyboardButton(text='Алексей Липцер', url='https://telegra.ph/Aleksej-Lipcer-10-22')

new_faces_kb =  InlineKeyboardMarkup(inline_keyboard=[[Bor_button], [Tona_button], [Kamardin_button],[Polina_button], [Mel_button],[Lipzer_button]])

###############################################################################################################

Kamardin_button_eng = InlineKeyboardButton(text='Artyom Kamardin', url='https://telegra.ph/Artyom-Kamardin-10-19-2')
Mel_button_eng = InlineKeyboardButton(text='Grigory Melkonyants', url='https://telegra.ph/Grigory-Melkonyants-10-19')
Polina_button_eng = InlineKeyboardButton(text='Polina Yevtushenko', url='https://telegra.ph/Polina-Yevtushenko-10-19')
Tona_button_eng = InlineKeyboardButton(text='Antonina Favorskaia', url='https://telegra.ph/Antonina-Favorskaia-10-19')
Bor_button_eng = InlineKeyboardButton(text='Igor Baryshnikov', url='https://telegra.ph/Igor-Baryshnikov-10-19-2')
Lipzer_button_eng = InlineKeyboardButton(text='Alexei Lipster', url='https://telegra.ph/Alexei-Lipster-10-22')

new_faces_eng_kb =  InlineKeyboardMarkup(inline_keyboard=[[Bor_button_eng], [Tona_button_eng], [Kamardin_button_eng],[Polina_button_eng], [Mel_button_eng], [Lipzer_button_eng]])

##########################################################################################################################


Kamardin_button_de = InlineKeyboardButton(text='Artem Kamardin', url='https://telegra.ph/Artem-Kamardin-10-19')
Mel_button_de = InlineKeyboardButton(text='Grigory Melkonyants', url='https://telegra.ph/Grigory-Melkonyants-10-19-2')
Polina_button_de = InlineKeyboardButton(text='Polina Ewtuschenko', url='https://telegra.ph/Polina-Ewtuschenko-10-19')
Tona_button_de = InlineKeyboardButton(text='Antonina Faworskaja', url='https://telegra.ph/Antonina-Faworskaja-10-19')
Bor_button_de = InlineKeyboardButton(text='Igor Baryschinikow', url='https://telegra.ph/Igor-Baryschinikow-10-19')
Lipzer_button_de = InlineKeyboardButton(text='Alexey Lipzer', url='https://telegra.ph/Alexey-Lipzer-10-22')

new_faces_de_kb =  InlineKeyboardMarkup(inline_keyboard=[[Bor_button_de], [Tona_button_de], [Kamardin_button_de],[Polina_button_de], [Mel_button_de], [Lipzer_button_de]])



#





