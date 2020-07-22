import mongoengine as me
import datetime

me.connect('CARS')

class Manufacturer(me.Document):
    name = me.StringField(min_length=2, max_length=128, required=True)
    created = me.DateField()

    def __str__(self):
        return str(self.id)


class  Vihicle(me.Document):
    COLOURS = (
        ('Black', 'Black'),
        ('White', 'White')
    )
    colour = me.StringField(choises=COLOURS, min_length=3, required=True)
    type_ = me.StringField(min_length=3, max_length=255)
    engine = me.StringField(min_length=3, max_length=512, required=True)
    manufacturer = me.ReferenceField(Manufacturer)


if __name__ == '__main__':
    bmw = Manufacturer.objects.create(name='BMW', created=datetime.date(1950, 6, 25))

    obj1 = Vihicle.objects.create(colour='Black', type_='car', engine='V-6', manufacturer=bmw)
    obj2 = Vihicle.objects.create(colour='White', type_='car', engine='V-8', manufacturer=bmw)

