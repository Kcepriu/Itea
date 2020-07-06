class Array:
    def __init__(self, type_, size):
        self._type = type_
        self._size = size

        self._data = [0] * self._size

    def __getitem__(self, item):
        if self._is_value_in_valid_range(item):
            return self._data[item]


    def _is_value_in_valid_range(self, value):
        if 0 <= value < self._size:
            return True
        raise IndexError

    def _is_valid_type(self, type_):
        if self._type == type_:
            return True
        raise TypeError

    def __setitem__(self, key, value):
        if self._is_value_in_valid_range(key) and self._is_valid_type(type(value)):
            self._data[key] = value



array = Array(int, 6)
array[5] = 100
print(array[5])

array[1] = 'fff'
print(array[1])

