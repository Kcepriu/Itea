'''Создать свою структуру данных Список, которая поддерживает
индексацию. Методы pop, append, insert, remove, clear. Перегрузить
операцию сложения для списков, которая возвращает новый расширенный
объект.'''

class List:
    def __init__(self, *args):
        self._data = list(args)

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __str__(self):
        return str(self._data)

    def _is_value_in_valid_range(self, value):
        if 0 <= value < len(self._data):
            return True
        raise IndexError

    def append(self, value):
        self._data[len(self._data):] = [value]

    def clear(self):
        self._data = []

    def pop(self, key=None):
        if not key:
            key = len(self._data) - 1

        if self._is_value_in_valid_range(key):
            value = self._data[key]
            self._data =self._data[:key]+self._data[key+1:]
            return  value

    #  insert, remove
if __name__ == '__main__':

    my_list = List(1, 2, 4 , 5)
    print(my_list)
    #
    my_list[1] = '123'
    print(my_list)

    my_list.append(456)
    print(my_list)

    print('pop', my_list.pop(10))
    print(my_list)

    # print(my_list[1])
    # print(my_list)

    # a = []
    # a[0] = 'fff'
    # print(a[100])