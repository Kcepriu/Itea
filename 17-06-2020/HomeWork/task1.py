"""1) Создать класс автомобиля. Описать общие аттрибуты. Создать
классы легкового автомобиля и грузового. Описать в основном
классе базовые аттрибуты для автомобилей. Будет плюсом если в
классах наследниках переопределите методы базового класса."""

class Car_common:
    def __init__(self, vin, make, year, owner = '', price=0):
        #Антон спитаю тут. А нема якихось рекомендацій, чи загальноприйнятих правил по передачі параметрів в клас?

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

class Car(Car_common):
    def __init__(self, vin, make, year, owner = '', price=0, body_style='sedan'):
        Car_common.__init__(self, vin, make, year, owner, price)
        self.body_style = body_style

    def print_info(self):
        Car_common.print_info(self)
        print('Body style -', self.body_style)



class Truck(Car_common):
    def __init__(self, vin, make, year, owner = '', price=0, max_carrying=0):
        Car_common.__init__(self, vin, make, year, owner, price)
        self.max_carrying = max_carrying

    def change_the_price(self, percent=5):
        '''По замовчанню на інший відсоток зміними ціну'''
        Car_common.change_the_price(self, percent)

    def print_info(self):
        Car_common.print_info(self)
        print('Max carrying -', self.max_carrying)


if __name__ == '__main__':
    car1 = Car('123456', 'Ford', '2012', '', 5000)


    car1.print_info()
    car1.new_owner('Julli')
    car1.print_info()
    car1.change_the_price(10)
    car1.print_info()

    car2 = Truck('98765', 'Volvo', '2019', '', 80000, 20000)

    car2.print_info()
    car2.change_the_price()
    car2.print_info()


