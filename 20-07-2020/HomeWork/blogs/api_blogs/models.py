import mongoengine as me
import datetime

me.connect('db_post_1')

class Author(me.Document):
    first_name = me.StringField(min_length=8, max_length=256, required=True)
    sur_name = me.StringField(min_length=8, max_length=256, required=True)


class Teg(me.EmbeddedDocument)
    teg_name = me.StringField(min_length=2, max_length=255, required=True, unique=True)

class Post(me.Document):
    name = me.StringField(min_length=2, max_length=255, required=True, unique=True)
    body = me.StringField(min_length=8, max_length=256, required=True)
    date_publication = me.DateTimeField()

    author =  me.ReferenceField(Author)
    author_name = me.StringField(min_length=1, max_length=256, required=True)

    count_viewing=me.IntField(min_value=0, default=0)

    teg = me.EmbeddedDocumentListField(Teg)

    def __init__(self):
        self.date_publication = datetime.datetime.now()