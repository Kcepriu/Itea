from  models import Products, Categories

class Initial_Data:
    data_from_init = {'products':[
        {'name': 'Телевізори LG 1', 'price': 13000.50, 'count': 10, 'availability': True, 'categorie': 'Телевізори LG'},
        {'name': 'Телевізори LG 2', 'price': 3000.80, 'count': 5, 'availability': True, 'categorie': 'Телевізори LG'},
        {'name': 'Телевізори LG 3', 'price': 1000.80, 'count': 0, 'availability': False, 'categorie': 'Телевізори LG'},

        {'name': 'Телевізори Samsung 1', 'price': 5100.80, 'count': 0, 'availability': False,
         'categorie': 'Телевізори Samsung'},
        {'name': 'Телевізори Samsung 2', 'price': 15100.80, 'count': 10, 'availability': True,
         'categorie': 'Телевізори Samsung'},

        {'name': 'Ноутбуки LG 1', 'price': 15100.80, 'count': 10, 'availability': True,
         'categorie': "Ноутбуки 14'' LG"},
        {'name': 'Ноутбуки LG 2', 'price': 21100.80, 'count': 3, 'availability': True,
         'categorie': "Ноутбуки 14'' LG"},
        {'name': 'Ноутбуки LG 3', 'price': 21100.80, 'count': 5, 'availability': True,
         'categorie': "Ноутбуки 14'' LG"},

        {'name': 'Ноутбуки Lenovo 1', 'price': 11100.00, 'count': 3, 'availability': True,
         'categorie': "Ноутбуки 14'' Lenovo"},

        {'name': 'Ноутбуки HP 1', 'price': 31100.00, 'count': 3, 'availability': True,
         'categorie': "Ноутбуки 15'' HP"},

    ],
                 'categories':[
                     {'category_name': 'Телевізори', 'description': 'Всі телеdізири', 'parent': None},
                     {'category_name': 'Телевізори LG', 'description': 'Телевізори марки LG', 'parent': 'Телевізори'},
                     {'category_name': 'Телевізори Samsung', 'description': 'Телевізори марки Samsung',
                      'parent': 'Телевізори'},

                     {'category_name': 'Ноутбуки', 'description': 'Всі Ноутбуки', 'parent': None},

                     {'category_name': "Ноутбуки 14''", 'description': "Всі Ноутбуки 14''", 'parent': 'Ноутбуки'},
                     {'category_name': "Ноутбуки 15''", 'description': "Всі Ноутбуки 15''", 'parent': 'Ноутбуки'},

                     {'category_name': "Ноутбуки 14'' LG", 'description': "Всі Ноутбуки 14'' LG",
                      'parent': "Ноутбуки 14''"},
                     {'category_name': "Ноутбуки 14'' Lenovo", 'description': "Всі Ноутбуки 14'' Lenovo",
                      'parent': "Ноутбуки 14''"},
                     {'category_name': "Ноутбуки 15'' HP", 'description': "Всі Ноутбуки 15'' HP",
                      'parent': "Ноутбуки 15''"}
                 ]}
    def initial_data(self):
        list_categories = self.data_from_init['categories']

        for elem in list_categories:
            name_category = elem['parent']
            if name_category:
                elem['parent'] = Categories.objects.get(category_name=name_category)
            Categories.objects.create(**elem)

        list_products = self.data_from_init['products']
        for elem in list_products:
            elem['categorie'] = Categories.objects.get(category_name=elem['categorie'])
            Products.objects.create(**elem)

if __name__ == '__main__':
    id = Initial_Data()
    id.initial_data()
