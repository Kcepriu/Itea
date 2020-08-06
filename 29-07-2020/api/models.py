import mongoengine as me



class Post(me.Document):
    title = me.StringField(min_length=2, max_length=255)
    body = me.StringField(min_length=2, max_length=255)
    created = me.DateField(default = )


class Author(me.Document):
    ligin = me.StringField(unique=True, min_length=6, max_length=255)
    password = me.StringField(min_length=5, max_length=255)
    post = me.ReferenceField(Post)