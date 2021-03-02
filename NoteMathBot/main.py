from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
import json

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

###############
#сам ботяра
@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    # m11 = InlineKeyboardButton("алгебра", callback_data='bt2')
    # m12 = InlineKeyboardButton("геометрия 😎", callback_data='bt1')
    # greet_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(m11, m12)
    if str(message.from_user.id) not in users:
        users[str(message.from_user.id)]= {"status":0}
        with open("data.json", "w") as write_file:
            json.dump(users, write_file)
        await message.answer("тут можно посмотреть все билеты по геометрии и другии теоремы \n \n выбери режим:")
    else:
        await message.answer("выбери режим:")
    print(users)

@dp.message_handler(content_types=['photo'])
async def photoes(message):
    global config

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

    config_txt.close()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)  # запуск

