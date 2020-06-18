"""Создать класс магазина. Конструктор должен инициализировать
значения: «Название магазина» и «Количество проданных
товаров». Реализовать методы объекта, которые будут увеличивать
кол-во проданных товаров, и реализовать вывод значения
переменной класса, которая будет хранить общее количество
товаров проданных всеми магазинами."""

class Shop:
    count = 0
    def __init__(self, name, count=0):
        self.name = name
        self.count = count
        Shop.count = count

    def add_count(self, count):
        self.count += count
        Shop.count += count

    def print_count_shop(self):
        print('Количество проданных товаров магазином  %s: %s шт.' % (self.name, self.count))

    def print_count_all_shop(self):
        print('Количество проданных товаров всеми магазинами: %s шт.' % Shop.count)


shop1 = Shop('Veronika')
shop2 = Shop('Viktoria', 10)

shop1.add_count(55)
shop2.add_count(13)

shop1.print_count_shop()
shop2.print_count_shop()

shop2.print_count_all_shop()