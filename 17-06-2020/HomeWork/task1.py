"""1) Создать класс автомобиля. Описать общие аттрибуты. Создать
классы легкового автомобиля и грузового. Описать в основном
классе базовые аттрибуты для автомобилей. Будет плюсом если в
классах наследниках переопределите методы базового класса."""

class Car:
    def __init__(self, vin, make, year, owner = '', price=0):
        self.vin   = vin
        self.make  = make
        self.year  = year
        self.price = price
        self.owner = owner

    def change_the_price(self, percent=10):
        self.price *= (100 - percent)/100

    def print_price(self):
        print('Car price (VIN %s) : %s $ ' % (self.vin, self. price) )

    def new_owner(self, owner):
        self.owner = owner

    def print_info(self):
        print('-'*10)
        print('Info car vin -', self.vin)
        print('Make -', self.make)
        print('Year -', self.year)
        print('Owner -', self.owner)
        print('Price -', self.price)

car1 = Car('123456', 'Ford', '2012', '', 5000)


car1.print_info()
car1.new_owner('Julli')
car1.print_info()
car1.change_the_price(10)
car1.print_info()

