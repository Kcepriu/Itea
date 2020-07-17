
class QueryFromTables:
    def __init__(self):
        self.query_create_tables = self.initial_query_create_tables()
        self.dict_query = self.initial_dict_query()

    def initial_query_create_tables(self):
        return {'categories': '''CREATE TABLE categories (
                                        id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name_categiry	TEXT UNIQUE)''',

                'product': '''CREATE TABLE product (
                                    id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name	TEXT NOT NULL,
                                    id_category	INTEGER NOT NULL,
                                    price	INTEGER DEFAULT 0,
                                    quantity	INTEGER DEFAULT 0,
                                    on_the_market	NUMERIC NOT NULL DEFAULT 0,
                                    FOREIGN KEY(id_category) REFERENCES categories(id))'''
                }

    def initial_dict_query(self):
        return {
            'select_all_categories': 'select id, name_categiry from categories',
            'select_categories_from_name': 'select id, name_categiry from categories where name_categiry=?',
            'select_product_from_name_category':'''select p.id, p.name, p.price, p.quantity, p.on_the_market, 
                                c.name_categiry from product  p
                    inner join categories c
                        on p.id_category = c.id
                    where p.quantity>0 and  c.name_categiry=?''',
            'select_product_from_id':'''select p.id, p.name, p.price, p.quantity, p.on_the_market, 
                                c.name_categiry from product  p
                    inner join categories c
                        on p.id_category = c.id
                    where p.id=?''',
            'insert_categories': 'INSERT INTO categories (name_categiry)  VALUES (?)',
            'insert_product': '''INSERT INTO product (name, id_category, price, quantity, on_the_market)
                                VALUES (?, ?, ?, ?, ?)'''
                }

    def query_test_data(self):
        return ["INSERT INTO categories (id, name_categiry) VALUES (1, 'Тарілки');",
                "INSERT INTO categories (id, name_categiry) VALUES (2, 'Чашки');",
                "INSERT INTO categories (id, name_categiry) VALUES (3, 'Ложки');",
                "INSERT INTO categories (id, name_categiry) VALUES (4, 'Вилки');",
                                
                """INSERT INTO product (id, name, id_category, price, quantity, on_the_market) 
                    VALUES (1, 'Тарілка кругла', 1, 50, 10, 1);""",
                """INSERT INTO product (id, name, id_category, price, quantity, on_the_market) 
                    VALUES (2, 'Тарілка овальна', 1, 88, 10, 0);""",
                """INSERT INTO product (id, name, id_category, price, quantity, on_the_market) 
                    VALUES (3, 'Тарілка трикутна', 1, 100, 0, 1);""",
                """INSERT INTO product (id, name, id_category, price, quantity, on_the_market) 
                    VALUES (4, 'Чашка для кави (чорна)', 2, 100, 10, 1);""",
                """INSERT INTO product (id, name, id_category, price, quantity, on_the_market) 
                    VALUES (5, 'Чашка для кави (біла)', 2, 100, 5, 1);""",
                """INSERT INTO product (id, name, id_category, price, quantity, on_the_market) 
                    VALUES (6, 'Чашка для кави (жовта)', 2, 110, 0, 1);""",
                """INSERT INTO product (id, name, id_category, price, quantity, on_the_market) 
                    VALUES (7, 'Чашка для кави (червона)', 2, 50, 10, 0);""",
                """INSERT INTO product (id, name, id_category, price, quantity, on_the_market) 
                    VALUES (8, 'Виделка десертна', 4, 10, 100, 1);""",
                """INSERT INTO product (id, name, id_category, price, quantity, on_the_market) 
                    VALUES (9, 'Виделка столова', 4, 11, 0, 1);""",
                """INSERT INTO product (id, name, id_category, price, quantity, on_the_market) 
                    VALUES (10, 'Виделка для устриць', 4, 12, 20, 0);"""]