import mongoengine as me

me.connect('db_internet_shop')

class Categorie(me.Document):
    category_name = me.StringField(min_length=2, max_length=255, required=True, unique=True)
    description = me.StringField(min_length=2, max_length=512)
    parent = me.ReferenceField('self')

    def __str__(self):
        return str(self.id)


class Product(me.Document):
    name = me.StringField(min_length=2, max_length=255, required=True)
    price = me.DecimalField(min_value=0, default=0)
    count = me.IntField(min_value=0, default=0)
    count_viewing = me.IntField(min_value=0, default=0)
    availability = me.BooleanField()
    categorie = me.ReferenceField(Categorie)

    def add_count(self, product_id=None):
        self.count_viewing += 1
        self.save()


