'''Создать бот для поиска статей на википедии.
При входе, бот запрашивает пользователя ввести имя статьи. Далее бот осуществляет этот поиск на википедии,
в случае отстутвия выводит соотвествующие сообщение, а если статья найдена выводит на экран текст. '''
import wikipedia
from telebot import TeleBot
from .config import TOKEN

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, GREETINGS, reply_markup=kb)
    bot.r