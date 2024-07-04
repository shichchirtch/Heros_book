from aiogram.types import CallbackQuery, Message
from aiogram.filters import BaseFilter
from pagination import pagin_dict
from aiogram.fsm.context import FSMContext
from last_words import *
from postgres_functions import check_user_in_table

class MOVE_PAGE(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data in ['forward', 'backward']:
            return True
        return False



class CHECK_NUMBER(BaseFilter):
    async def __call__(self, message: Message, state: FSMContext):
        print("WORKs check number filter")
        bot_state = await state.get_state()
        dict_key = bot_state.split(':')[1]
        dict_collection = {
                           'kriger': kriger,
                           'gorinov': gorinov,
                           'kara_murza': kara_murza,
                           'yashin': yashin,
                           'navalny': navalny,
                           'pivovarov': pivovarov,
                           'base_part': pagin_dict,
                           'skolichenko': skolichenko,
                           'moskalev': moskalev,
                           'simonov': simonov,
                           'ivanov': ivanov,
                           'afanasyev': afanasyev,
                           'gutnikova': gutnikova,
                           'uvarov': uvarov,
                           'kamardin': kamardin,
                           'petrova': petrova,
                           'orlov': orlov,
                           'chanysheva': chanysheva,
                           'galyamina': galyamina,
                           'baryshnikov': baryshnikov,
                           'ponomarenko': ponomarenko
                           }

        using_dict = dict_collection[dict_key]

        if (message.text.startswith('/') and message.text[1:].isdigit()
                and 0 < int(message.text[1:]) < len(using_dict)):
            return True
        elif message.text.isdigit() and 0 < int(message.text) <= len(using_dict):
            return True
        else:
            print('CHECK NUMBER RETURN FALSE')
            return False



class PRE_START(BaseFilter):
    async def __call__(self, message: Message):
        print("PRE_START Filter works")
        user_tg_id = message.from_user.id
        if await check_user_in_table(user_tg_id):
            return False
        return True

class IS_DIGIT_CALLBACK_DATA(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.isdigit()


class IS_DEL_BUCKMARK(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        print('Works IS_DEL_BUCKMARK')
        return callback.data.endswith('del') and callback.data[:-3].isdigit()