from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis
from config import settings

using_redis = Redis(host=settings.REDIS_HOST)
redis_storage = RedisStorage(redis=using_redis)



class FSM_NAMES(StatesGroup):
    base_part = State()
    kriger = State()
    gorinov = State()
    yashin = State()
    kara_murza = State()
    navalny = State()
    pivovarov = State()
    skolichenko = State()
    moskalev = State()
    simonov = State()
    ivanov = State()
    afanasyev = State()
    gutnikova = State()
    kamardin = State()
    uvarov = State()
    petrova = State()
    orlov = State()
    chanysheva = State()
    galyamina = State()
    baryshnikov = State()
    ponomarenko = State()
    otzyv = State()
    waiting = State()



