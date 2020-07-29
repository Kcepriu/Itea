from telebot import TeleBot, types
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton)

from .config import TOKEN
from .work_with_data import WorkWithData as wwd

bot = TeleBot(TOKEN)

@bot.message_handler(content_types=['text'], commands=['start'])
def start(message):
    # Перевірити чи існує такий користувач. Якщо ні, додати його
    if wwd.add_user(message.from_user):
        return_message = f'Hello {message.from_user.first_name} {message.from_user.last_name}'
    else:
        return_message = 'Error'

    bot.send_message(message.from_user.id, 'Прийом заявки')

    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = KeyboardButton(f'{message.from_user.first_name} {message.from_user.last_name}')
    kb.add(button1)
    bot.send_message(message.from_user.id, 'Введите ваше имя', reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def clic_car(call):
    print(call.data)
    bot.send_message(call.message.chat.id, call.message.text)

@bot.message_handler(content_types=['text'])
def hello(message):
    print(message)
    bot.send_message(message.from_user.id, message.text)
