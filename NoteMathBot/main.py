from aiogram import Bot, Dispatcher, executor, types
import datd
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import json
import os


#подгружаем JSON с юзерами
users = {}
with open("data.json", "r") as read_file:
    users = json.load(read_file)
print(users)

###############
#расшифровываем конфиг с данными о боте
config_txt = open('config.txt', 'r')
config = config_txt.read().split('\n')
config_txt.close()
###############
# инициализация бота

bot = Bot(token=(config[0]))
dp = Dispatcher(bot)

delay = 0
###############
#сам ботяра
@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    b_fiz = KeyboardButton('математика 💣')
    b_math = KeyboardButton('физика 👋')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    greet_kb.row(b_fiz,b_math)
    if str(message.from_user.id) not in users:
        users[str(message.from_user.id)]= {"status":0}
        with open("data.json", "w") as write_file:
            json.dump(users, write_file)
        await message.answer("тут можно посмотреть все билеты по геометрии и другии теоремы \n \n выбери режим:", reply_markup=greet_kb)
    else:
        await message.answer("выбери режим:", reply_markup=greet_kb)
    print(users)

@dp.message_handler(content_types=['photo'])
async def photoes(message):
    global config
    global delay

    new = str(int(config[1])+1)
    await message.photo[-1].download(new+'.jpg')
    config_txt = open('config.txt', 'r+')
    cn = config_txt.read()
    cnn = cn.split('\n')
    cn = ''
    cnn[1] = new
    config = cnn
    cnn.pop(-1)
    for i in cnn:
        cn+=i+'\n'
    print(cn)
    config_txt.seek(0)
    config_txt.write(cn)
    datd.add_image(new)
    config_txt.close()
    delay = new

@dp.message_handler(content_types=['text'])
async def maint(message : types.Message):
    global delay
    if delay != 0:
        datd.add_text(delay, message.text)
        delay = 0
        await bot.send_message(message.from_user.id, 'Приnal')
    else:
        if message.text[0] == '/':
            num = message.text[1:]
            inf = datd.get(num)
            await bot.send_message(message.from_user.id, inf[1])
            f = open(inf[0], "rb")
            await Bot.send_photo(self=bot, chat_id=message.from_user.id, photo=f)
            f.close()
            await bot.send_message(message.from_user.id, inf[2])
            markdown = """
                            *bold text*
                            _italic text_
                            [text](URL)
                            """

            await bot.send_message(message.from_user.id, "использованные материалы\n"+inf[5])
        elif message.text == 'физика 👋':
            await message.answer("патом")
        elif message.text == 'математика 💣':

            b_fiz = KeyboardButton('билеты 🤩')
            b_math = KeyboardButton('новые теоремы')
            greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            greet_kb.row(b_fiz, b_math)
            await message.answer(reply_markup=greet_kb)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)  # запуск

