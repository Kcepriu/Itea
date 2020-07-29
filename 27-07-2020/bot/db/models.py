import mongoengine as me

me.connect('botCars')

class Car(me.Document):
    title = me.StringField(min_length=1, max_length=256)
    photo = me.FileField()

    def __str__(self):
        pass

