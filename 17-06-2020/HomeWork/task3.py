"""Создать класс точки, реализовать конструктор который
инициализирует 3 координаты (Class): Определенный программистом тип данных.x, y, z).
    1. Реалзиовать методы для получения и изменения каждой из координат.
    2. Перегрузить для этого класса методы сложения, вычитания, деления умножения.
    3. Перегрузить один любой унарный метод.

Ожидаемый результат: умножаю точку с координатами 1,2,3 на
другую точку с такими же координатами, получаю результат 1, 4, 9."""

class Point:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def get_coordinate(self, name):
        #return self.__dict__[name]
        return getattr(self, name)

    def set_coordinate(self, name, value):
        self.__dict__[name] = value

    def __add__(self, other):
        return Point(self.x + other.x,  self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self, other):
        try:
            return Point(self.x / other.x, self.y / other.y, self.z / other.z)
        except ZeroDivisionError:
            #Антон. Спитаю тут. Що зазвичай в таких ситуаціях робити, Треба виводити якесь повідомлення? Наскільки коректно повертати None?
            return None
    def __neg__(self):
        return Point(-self.x , -self.y , -self.z)


    def __str__(self):
        return '('+ str(self.x) + ', ' + str(self.y)+ ', ' + str(self.z)+')'

if __name__ == '__main__':
    point1 = Point(0, 1, 2)
    point2 = Point(5, 6, 4)

    name='y'

    print(name+' = ', point1.get_coordinate(name))

    point1.set_coordinate(name, 10)
    print(name+' = ', point1.get_coordinate(name))


    print('-'*10)
    point_add = point1+point2
    print(point1, ' + ', point2, ' = ', point_add)

    point_sub = point1-point2
    point_mul = point1*point2
    point_truediv = point1/point2

    print(point1, ' - ', point2, ' = ', point_sub)
    print(point1, ' * ', point2, ' = ', point_mul)
    print(point1, ' / ', point2, ' = ', point_truediv)

    point2.set_coordinate('z', 0)
    point_truediv_err = point1/point2
    print(point1, ' / ', point2, ' = ', point_truediv_err)


    print('-',point1, '=', -point1)
    print('-',point_sub, '=', -point_sub)
    print('-',point_truediv, '=', -point_truediv)
