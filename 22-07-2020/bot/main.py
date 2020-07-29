from telebot import TeleBot
from .congig import TOKEN

bot = TeleBot(TOKEN)

@bot.message_handler(content_types=['text'], commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Прийом заявки')
    bot.send_message(message.from_user.id, 'Введите ваше имя')

@bot.message_handler(content_types=['text'])
def hello(message):
    bot.send_message(message.from_user.id, message.text)

# def start_bot()