from telebot import TeleBot, types
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

    print(return_message)
    bot.send_message(message.from_user.id, return_message)

@bot.message_handler(content_types=['text'])
def hello(message):
    # bot.send_message(message.from_user.id, message.text)
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keys = []
    for i in range(10):
        keys.append(types.InlineKeyboardButton(text=str(i),
                                               callback_data=str(f"call_{i}")))
    keyboard.add(*keys)
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима",
                     reply_markup=keyboard)
