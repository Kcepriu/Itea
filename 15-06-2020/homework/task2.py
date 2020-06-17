"""2) СОздать словарь Страна:Столица. Создать список стран. Не все страны со списка должны сходиться с названиями стран
со словаря. С помощою оператора in проверить на вхождение элемента страны в словарь, и если такой ключ действительно
существует вывести столицу."""


country_capital={
    'Japan':    'Tokyo',
    'Austria':  'Vienna',
    'Poland':   'Warsaw',
    'Estonia':  'Tallinn'
}

capitals = ['Austria', 'Iran', 'Poland', 'Sweden']

for capital in capitals:
    if capital in country_capital:
        print(country_capital[capital])