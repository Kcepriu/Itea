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

    def _is_value_in_valid_range(self, value, text_error=''):
        if 0 <= value < len(self._data):
            return True
        raise IndexError(text_error)

    def append(self, value):
        self._data[len(self._data):] = [value]

    def clear(self):
        self._data = []

    def pop(self, key=None):
        if key is None:
            key = len(self._data) - 1

        if self._is_value_in_valid_range(key, 'pop index out of range'):
            value = self._data[key]
            self._data =self._data[:key]+self._data[key+1:]
            return  value

    def insert(self, key, value):
        self._data = self._data[:key]+[value]+self._data[key:]

    def remove(self, value):
        if not value in self._data:
            raise ValueError('List.remove(x): x not in list')
        self.pop(self._data.index(value))

    def __add__(self, other):
        return List(*(self._data + other._data))


if __name__ == '__main__':

    my_list = List(1, 2, 5, 2)
    my_list_2 = List('dd', 'ff', 'gg')

    print(my_list)


    new_list = my_list + my_list_2

    print(new_list[2])
    print(type(new_list))
