'''Создать свою структуру данных Словарь, которая поддерживает методы,
get, items, keys, values. Так же перегрузить операцию сложения для
словарей, которая возвращает новый расширенный объект.'''

class Dict:
    def __init__(self, *args):
        self._data = dict(args)

    def __str__(self):
        return str(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

    def get(self, key, default=None):
        try:
            result = self._data[key]
        except KeyError:
            result = default
        return result

    def items(self):
        return [(key, self._data[key]) for key in self._data]

    def keys(self):
        return [key for key in self._data]

    def values(self):
        return [self._data[key] for key in self._data]

    def __add__(self, other):
        return Dict(*(self.items()  + other.items()))

if __name__ == '__main__':

    my_dict = Dict((1, 'aa'), (2, 'bb'), (4, 'cc'))
    # my_dict = Dict()

    print(my_dict)
    my_dict['key'] = 333
    print(my_dict)
    my_dict[2] = 444
    print(my_dict)
    print(my_dict.get('key', 'ddd'))
    print(my_dict.items())

    for x, y in my_dict.items():
        print(x, y)

    print(my_dict.keys())
    print(my_dict.values())

    my_dict2 = Dict(('key1', '111'), ('key2', '222'), ('key3', '33'))

    my_dic3 = my_dict + my_dict2

    print(my_dic3)
