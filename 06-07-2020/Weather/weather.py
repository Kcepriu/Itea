import requests
from bs4 import BeautifulSoup
import datetime
import re

class MyWeatherError(Exception):
    pass

class Error404(MyWeatherError):
    pass

class ErrorCityNotFound(MyWeatherError):
    pass

class ErrorDate(MyWeatherError):
    pass

class ErrorFormatDate(MyWeatherError):
    pass

class Sinoptik():
    def __init__(self):
        super().__init__()
        self._url = 'https://sinoptik.ua'
        self._default_city = 'киев'
        self._headers = requests.utils.default_headers()
        self._headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})

    def get_html(self, url):
        r = requests.get(url)
        return r.text

    def get_weather(self, city=None, date=None):
        if date:
            if not re.findall('[1-2]\d\d\d-[0-1]\d-[0-3]\d', date):
                raise ErrorFormatDate


        url = self._url+'/погода-'+(city if city else self._default_city)+('/'+date if date else '')

        html = self.get_html(url)
        soup = BeautifulSoup(html, 'lxml')

        #Якщо дата є, то можливо проблема саме в даті а не місті
        #Треба спробувати підключитись без дати, тоді точно знатимемо що проблема в місті
        if soup.find('div', class_='r404'):
            if date:
                try:
                    self.get_weather(city)
                except ErrorCityNotFound:
                    raise ErrorCityNotFound
                else:
                    raise ErrorDate
            else:
                raise ErrorCityNotFound

        block_day = soup.find('div', id="blockDays")
        current_name_block = block_day.get('class')

        current_block = block_day.find('div', class_='main', id=current_name_block[0])

        description = current_block.find('div', class_='weatherIco').get('title')
        min_temp = current_block.find('div', class_='min').find('span').text
        max_temp = current_block.find('div', class_='max').find('span').text

        return {'description':description, 'min_temp':min_temp, 'max_temp':max_temp}

    #Винести в програму обробки класу
    def return_weather(self, city=None, date=None):
        try:
            metcast = self.get_weather(city=city, date=date)
        except ErrorCityNotFound:
            return 'Город указан не верно'
        except ErrorDate:
            return 'Нет данных на выбранную дату'
        except ErrorFormatDate:
            return 'Не верный формат даты'
        else:
            now = datetime.datetime.now()
            _city = city if city else self._default_city
            _date = date if date else now.strftime("%Y-%m-%d")

            return  f"""Прогноз погоды по г. {_city} на {_date} число:
                \tОписание: {metcast['description']}
                \tМинимальная температура: {metcast['min_temp']}
                \tМаксимальная температура: {metcast['max_temp']}"""

#689b01c43ded4804a84027bf54dc0817


if __name__ == '__main__':
    sinoptic = Sinoptik()
    # sinoptic.print_weather('Чернигов', '2020-07-20')
    print(sinoptic.return_weather())

