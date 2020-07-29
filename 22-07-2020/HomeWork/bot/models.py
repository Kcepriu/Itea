'''Написать бота-консультанта, который будет собирать информацию с
пользователя (его ФИО, номер телефона, почта, адресс, пожелания).
Записывать сформированную заявку в БД (по желанию SQl/NOSQL).).'''

import mongoengine as me
import datetime

me.connect('db_bot_1')

class User(me.Document):
    user_id = me.IntField(unique=True, required=True)
    first_name = me.StringField(min_length=2, max_length=255)
    last_name = me.StringField(min_length=2, max_length=255)
    username = me.StringField(min_length=2, max_length=255, required=True, unique=True)

class Request(me.Document):
    user = me.ReferenceField(User)
    user_name = me.StringField()
