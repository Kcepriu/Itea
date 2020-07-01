# a = [1, 2, 3]
#
# # print(type(type(type(a))))
# def beep(self):
#     return 'beep'
#
# MyClass = type('Car', (), {'car_type': 'Truck', 'beep': beep})
#
# car = MyClass()
#
# print(car.car_type)
# print(car.beep)

class MyMetaClass(type):
    black_list_name = 'get_b'
    def __new__(cls, name, base, attrs):
        if cls.black_list_name in attrs:
            raise ValueError(f'You cannot {cls.black_list_name}')
        print(cls, name, base, attrs)

        attrs.update({'cfreate_by':MyMetaClass})
        name = 'CreateByMyMetaclass'+name
        return super().__new__(cls, name, base, attrs)

class MyClass(metaclass=MyMetaClass):
    def __init__(self, a):
        self._a = a

    def get_a(self):
        return self.a

MyClass(1)
print(MyClass.cfreate_by)
print(MyClass.__name__)