from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove)

from mongoengine.errors import ValidationError

from .models import User, Request

from .config import TOKEN
from .texts import STEPS, APPLY, ACCEPT, APPLY_BT, ERROR_FORMAT

bot = TeleBot(TOKEN)

@bot.message_handler(content_types=['text'], commands=['start'])
def start(message):
    make_step(message, True)

@bot.message_handler(content_types=['text'])
def app_processing(message):
    make_step(message)

def make_step(message, start=None):
    user = User.get_user(chat=message.chat)

    if start or message.text == APPLY:
        user.active_request = None

    request = Request.get_request(user)

    if 0 < request.number_step <= len(STEPS):
        # Обработать запрос
        request[STEPS[request.number_step - 1]['field_name']] = message.text

    # Виводимо текст повідомлення
    if request.number_step >= len(STEPS):
        # Закінчили приймати заявку
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton(APPLY))

        text_message = APPLY_BT
        if request.number_step == len(STEPS):
            text_request = f'{ACCEPT}\n{str(request)}'
            bot.send_message(message.chat.id, text_request, reply_markup=None)
            request.number_step += 1

    else:
        # Знаходимось в процесі прийняття заявки
        kb = None
        if request.number_step == 0 and (user.first_name or user.last_name):
            # Для полегшення вводу спробуємо взяти імʼя із профілю і вивести кнопкою
            kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            kb.add(KeyboardButton(f'{user.last_name} {user.first_name}'))
        text_message = STEPS[request.number_step]['text']
        request.number_step += 1

    try:
        request.save()
    except ValidationError:
        text_message = f"{ERROR_FORMAT}\n{STEPS[request.number_step-2]['text']}"

    user.save()

    bot.send_message(message.chat.id, text_message, reply_markup=kb if kb else ReplyKeyboardRemove())

