from abc import ABC, abstractmethod

class FFF(Exception):
    pass


class AbstractCar(ABC):
    AVALIBLE_COLOUR = ('Red', 'Yellow')

    def __init__(self, colour, engine):
        self._colour = colour
        self._engine = engine


    # def get_colour(self):
    #     return self._colour


    @property
    def colour(self):
         return self._colour

    @colour.setter
    def colour(self, value):
        if value in AbstractCar.AVALIBLE_COLOUR:
            self._colour = value
        else:
            raise FFF

    def get_engine(self):
        return self._engine

    def set_engine(self, value):
        self._engine = value

    def del_anginne(self):
        self._engine = None
    #другий спосіб щоб без декораторів
    engine = property(get_engine, set_engine, del_anginne)

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def open_dour(self):
        pass


class Car(AbstractCar):
    def drive(self):
        print(f'Drive  {self._colour}')

    def open_dour(self):
        pass

car1 = Car('blak', 'ggg')

print(car1.colour)

car1.colour = 'Yellow'

print(car1.colour)

print(car1.engine)
car1.engine = 'v-6'
print(car1.engine)

del(car1.engine)
print(car1.engine)