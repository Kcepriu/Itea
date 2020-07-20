import mongoengine as me

me.connect('db_users')


class User(me.Document):
    login = me.StringField(min_length=2, max_length=255, required=True, unique=True)
    password = me.StringField(min_length=8, max_length=256, required=True)
    password_confirmation = me.StringField(min_length=8, max_length=256, required=True)
