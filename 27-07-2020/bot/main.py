from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton)
from .config import TOKEN, SEPARATOR
from .texts import GREETINGS, CHOIS_CAR
from .keyboards import START_KB

from .db.models import Car




bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    # button1 = KeyboardButton(START_KB['list_of_cars'])
    # button2 = KeyboardButton(START_KB['special_offers'])

    # kb.add(button1, button2)
    # buttons = [KeyboardButton(button, request_contact=True) for button in START_KB.values()]
    buttons = [KeyboardButton(button) for button in START_KB.values()]
    kb.add(*buttons)

    bot.send_message(message.from_user.id, GREETINGS, reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data.split(SEPARATOR)[0] == Car.__name__)
def clic_car(call):
    print(call.data)
    car_obj = Car.objects.get(id=call.data.split(SEPARATOR)[1])

    bot.send_photo(call.message.chat.id, car_obj.photo.read(), caption=car_obj.title)



# @bot.message_handler(content_types=['text'])
@bot.message_handler(func=lambda m: m.text == START_KB['list_of_cars'])
def list_of_car(message):
    kb = InlineKeyboardMarkup()
    # button = InlineKeyboardButton('Google', url='https://gogle.com')
    # kb.add(button)
    # bot.send_message(message.chat.id, CHOIS_CAR, reply_markup=kb)

    cars = [
        InlineKeyboardButton(
            car.title,
            callback_data=f'{Car.__name__}{SEPARATOR}{car.id}'
        ) for car in Car.objects()
    ]
    kb.add(*cars)
    bot.send_message(message.chat.id, CHOIS_CAR, reply_markup=kb)
