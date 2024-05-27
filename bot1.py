from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN_API = '7093417431:AAFkqbjVY-eXeQOFeB8_c_JXf0RusVsLVnc'
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)
'1234567890'
keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
button = KeyboardButton('кнопка1')
button2 = KeyboardButton('кнопка2')
button3 = KeyboardButton('кнопка3')
keyboard.add(button, button2, button3)


async def set_comands(bot: Bot): #меню с командами
    commands = [
        types.BotCommand(command='/start', description= 'начать работу бота')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(massege: types.Message):
    await massege.answer('Привет,я твой бот!',reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'кнопка1')
async def button_click(message: types.Message):
    await message.answer('Держи! Не теряй нас')

@dp.message_handler(lambda message: message.text == 'кнопка2')
async def button_click(message: types.Message):
    await message.answer('Держи! Не теряй на2')

@dp.message_handler(lambda message: message.text == 'кнопка3')
async def button_click(message: types.Message):
    await message.answer('Держи! Не теряй нас3')



async def on_startup(dispatcher): #меню с командами
    await set_comands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates= True, on_startup= on_startup)