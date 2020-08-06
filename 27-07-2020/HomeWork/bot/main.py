'''Создать бот для поиска статей на википедии.
При входе, бот запрашивает пользователя ввести имя статьи. Далее бот осуществляет этот поиск на википедии,
в случае отстутвия выводит соотвествующие сообщение, а если статья найдена выводит на экран текст. '''

import wikipedia
from wikipedia.exceptions import DisambiguationError
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton)
from telebot import TeleBot

from .config import TOKEN
from .texts import INPUT_NAME, WIKI, ERROR_QUERY

bot = TeleBot(TOKEN)

@bot.message_handler(content_types=['text'], commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, INPUT_NAME)

@bot.message_handler(content_types=['text'])
def working(message):
    kb = None

    wikipedia.set_lang("uk")
    search_el = wikipedia.search(message.text)
    if not search_el:
        bot.send_message(message.chat.id, f'По запросу "{message.text}" статей не найдено', reply_markup=kb)
        bot.send_message(message.chat.id, INPUT_NAME, reply_markup=kb)
        return

    if len(search_el) == 1:
        get_message(message.chat.id, search_el[0])
        return

    buttons = []
    i = 0
    for elem in search_el:
        buttons.append(InlineKeyboardButton(elem,callback_data=f'{WIKI}{i}'))
        i += 1

    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(*buttons)
    bot.send_message(message.chat.id, f'По запросу "{message.text}" найдено несколько статей', reply_markup=kb)

@bot.callback_query_handler(func=lambda call: call.data[0:4] == WIKI)
def clic_item(call):
    nom = int(call.data[4:])
    name_item=call.message.json['reply_markup']['inline_keyboard'][nom][0]['text']

    get_message(call.message.chat.id, name_item)

def get_message(id, name_item):
    wikipedia.set_lang("uk")
    try:
        item = wikipedia.page(name_item, auto_suggest=False)
    except DisambiguationError:
        item = ERROR_QUERY

    text_item = item.content

    if len(text_item) > 4096:
        for x in range(0, len(text_item), 4096):
            bot.send_message(id, text_item[x:x + 4096])
    else:
        bot.send_message(id, text_item)





