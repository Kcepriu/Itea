import mongoengine as me
import datetime

me.connect('db_post_1')

class Author(me.Document):
    first_name = me.StringField(min_length=1, max_length=256, required=True)
    sur_name = me.StringField(min_length=1, max_length=256, required=True)

    def __str__(self):
        return str(self.id)

class Teg(me.Document):
    # Осознано назвав teg_name. Так я к я хочу це імʼя зберігати і в TegField. А там буде зберігатись і teg
    teg_name = me.StringField(min_length=2, max_length=255, required=True, unique=True)

    def __str__(self):
        return str(self.id)


class TegField(me.EmbeddedDocument):
    teg = me.ReferenceField(Teg)
    teg_name = me.StringField(min_length=2, max_length=255, required=True)


class Post(me.Document):
    name = me.StringField(min_length=2, max_length=255, required=True)
    body = me.StringField(min_length=8, max_length=512, required=True)
    date_publication = me.DateTimeField(default=datetime.datetime.now())

    author =  me.ReferenceField(Author)
    author_name = me.StringField(min_length=1, max_length=256, required=True)

    count_viewing=me.IntField(min_value=0, default=0)

    teg = me.EmbeddedDocumentListField(TegField)

    def add_count(self):
        self.count_viewing += 1
        self.save()
