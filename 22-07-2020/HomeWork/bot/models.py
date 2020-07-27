'''Написать бота-консультанта, который будет собирать информацию с
пользователя (его ФИО, номер телефона, почта, адресс, пожелания).
Записывать сформированную заявку в БД (по желанию SQl/NOSQL).).'''

import mongoengine as me
import datetime

me.connect('db_post_1')

class Users(me.Document):
    pass

class Request(me.Document):
    user = me.ReferenceField(Users)
    user_name = me.StringField()

    pass