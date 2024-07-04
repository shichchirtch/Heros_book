from aiogram.types import BotCommand
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Функция для настройки кнопки Menu бота
async def set_main_menu(bot):
    # Создаем список с командами и их описанием для кнопки menu
    # bot
    main_menu_commands = [
        BotCommand(command='/exit',
                   description='Return to Faces list'),
        BotCommand(command='/continue',
                   description='Return to reading'),
        BotCommand(command='/bookmarks',
                   description='Bookmarks'),
        BotCommand(command='/help',
                   description='Bot commands'),
        BotCommand(command='/about_project',
                   description='Go to Beginning')
    ]

    await bot.set_my_commands(main_menu_commands)

pre_start_button = KeyboardButton(text='/start')

pre_start_clava = ReplyKeyboardMarkup(
    keyboard=[[pre_start_button]],
    resize_keyboard=True,
    input_field_placeholder='Приятного чтения'
)