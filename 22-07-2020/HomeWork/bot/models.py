'''Написать бота-консультанта, который будет собирать информацию с
пользователя (его ФИО, номер телефона, почта, адресс, пожелания).
Записывать сформированную заявку в БД (по желанию SQl/NOSQL).).'''

import mongoengine as me
import datetime

me.connect('db_bot_1')

class Request(me.Document):
    user = me.ReferenceField('User')
    user_name = me.StringField()
    tepelhone = me.StringField(min_length=10, max_length=12, regex='^[0-9]*$')
    email = me.StringField(min_length=6, max_length=255, regex='^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
    adress = me.StringField(min_length=2, max_length=255)
    texts = me.StringField(min_length=2, max_length=1024)
    number_step = me.IntField(default=0)

    @staticmethod
    def get_request(user):
        if user.active_request:
            return user.active_request

        request = Request.objects.create(user=user)
        user.active_request = request
        user.save()
        return request

    def __str__(self):
        return f'\tФИО:\t {self.user_name}\n' \
               f'\tНомер телефона:\t {self.tepelhone}\n' \
               f'\tE-mail:\t {self.email}\n' \
               f'\tАдресс:\t {self.adress}\n' \
               f'\tПожелание:\t {self.texts}\n'


class User(me.Document):
    user_id = me.IntField(unique=True, required=True)
    first_name = me.StringField(min_length=2, max_length=255)
    last_name = me.StringField(min_length=2, max_length=255)
    active_request = me.ReferenceField(Request)

    @staticmethod
    def get_user(chat):
        user = User.objects(user_id=chat.id)
        if not user:
            user = User.objects.create(user_id=chat.id, first_name=chat.first_name if chat.first_name else '' ,
                                       last_name=chat.last_name if chat.last_name else '')
        else:
            user = user[0]

        return user


