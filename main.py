import telebot
from telebot import types
import json


with open('token', 'r') as secret:
    token = secret.read()
bot = telebot.TeleBot(token)


with open('messages.json', 'r') as messages_json:
    messages = json.load(messages_json)


def rent_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    webapp = types.WebAppInfo('https://outcinema.ru')
    btn1 = types.KeyboardButton("Забронировать время", web_app=webapp)
    btn2 = types.KeyboardButton("Прочитать правила")
    btn3 = types.KeyboardButton("Задать вопрос")
    keyboard.add(btn1, btn2, btn3)
    return keyboard


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text=messages["start_message"].format(message.from_user),
                     reply_markup=rent_keyboard())


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Задать вопрос":
        bot.send_message(message.from_user.id, text=messages["question_message"])
    elif message.text == "Прочитать правила":
        bot.send_message(message.from_user.id, text=messages["rules_message"])


bot.polling(none_stop=True, interval=0)
