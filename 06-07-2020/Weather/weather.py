import requests
from bs4 import BeautifulSoup
import datetime
import re
import json
from abc import ABC, abstractmethod

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
class ErrorInvalidApiKey(MyWeatherError):
    pass


class MyWeather:
    def __init__(self):
        self._url = ''
        self._default_city = 'Киев'

    def _get_html(self, url):
        r = requests.get(url)
        return r.text

    @abstractmethod
    def get_weather(self, city_name=None, date=None):
        if date:
            if not re.findall('[1-2]\d\d\d-[0-1]\d-[0-3]\d', date):
                raise ErrorFormatDate

    def return_str_weather(self, city_name=None, date=None):
        try:
            metcast = self.get_weather(city_name, date)
        except ErrorCityNotFound:
            return 'Город указан не верно'
        except ErrorDate:
            return 'Нет данных на выбранную дату'
        except ErrorFormatDate:
            return 'Не верный формат даты'
        else:
            str_metcast=''
            for i, dict_tm in metcast['metcast'].items():
                str_metcast +=f"\t{i}\n\t\tТемпература: {dict_tm['temp']}\n\t\tОписание:{dict_tm['weather_description']}\n"

            return f"Прогноз погоды по г.{city_name if city_name else self._default_city}  на {metcast['date']}\n{str_metcast}"


class Sinoptik(MyWeather):
    def __init__(self):
        super().__init__()
        self._url = 'https://sinoptik.ua'
        self._headers = requests.utils.default_headers()
        self._headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})

    def get_weather(self, city=None, date=None):
        super().get_weather(city, date)

        url = self._url+'/погода-'+(city if city else self._default_city)+('/'+date if date else '')

        html = self._get_html(url)
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

        current_block = block_day.find('div', class_ = 'Tab', id = current_name_block[0]+'c')
        weather_details_block = current_block.find('table', class_ = 'weatherDetails')

        table_time = weather_details_block.find('tr', class_ = 'gray time')
        table_description = weather_details_block.find('tr', class_ = 'img weatherIcoS')
        table_temperature = weather_details_block.find('tr', class_ = 'temperature')

        list_time = []
        list_temp = []
        list_descr = []

        times = table_time.find_all('td')
        for tm in times:
            list_time.append(tm.text)

        temperatures = table_temperature.find_all('td')
        for tm in temperatures:
            list_temp.append(tm.text)

        descriptions = table_description.find_all('div', class_='weatherIco')
        for tm in descriptions:
            list_descr.append(tm.get('title'))

        dict_result ={}
        for time, temp, desc in zip(list_time, list_temp, list_descr):
            dict_result[time]={'temp': temp, 'weather_description': desc}

        date = date if date else datetime.datetime.now().strftime("%Y-%m-%d")
        return {'date':date, 'metcast':dict_result}

class OpenWeather(MyWeather):
    def __init__(self, api):
        super().__init__()
        self._url='http://api.openweathermap.org/data/2.5/forecast'
        self._api = api
        self._add_param= '&units=metric&lang=ru'


    def get_weather(self, city_name=None, date=None):
        if not city_name:
            city_name = self._default_city

        now = datetime.datetime.now()
        date = date if date else now.strftime("%Y-%m-%d")

        url=f'{self._url}?q={city_name}{self._add_param}&appid={self._api}'
        html = self._get_html(url)

        dict_weather = self.parsing_result(html)

        if not date in  dict_weather:
            raise ErrorDate

        return {'date': date, 'metcast': dict_weather[date]}


    def parsing_result(self, text):
        dict_result = json.loads(text)

        if dict_result.get('cod', 404) != '200':
            if dict_result.get('message', '') == 'city not found':
                raise ErrorCityNotFound
            elif 'Invalid API key' in dict_result.get('message', '') :
                raise ErrorInvalidApiKey
            else:
                raise ConnectionError

        result_weather = {}
        for item in dict_result.get('list', []):
            date_time_item = item.get('dt_txt', '')
            date_item = date_time_item[:10]
            time_item = date_time_item[11:]

            temp = item['main']['temp']
            temp_min = item['main']['temp_min']
            temp_max = item['main']['temp_max']
            weather_description = item['weather'][0]['description']

            weather_date = result_weather.get(date_item, {})
            weather_date[time_item] = {'temp': temp, 'weather_description': weather_description}
            result_weather[date_item] = weather_date

        return result_weather

if __name__ == '__main__':
    sinoptic = Sinoptik()
    open_weather = OpenWeather('689b01c43ded4804a84027bf54dc0817')


    # print(open_weather.return_str_weather('Чернигов', '2020-07-20'))
    # print(sinoptic.return_str_weather('Чернигов', '2020-07-20'))

    # print(open_weather.return_str_weather('Чернигов', '2020-07-29'))
    # print(sinoptic.return_str_weather('Чернигов', '2020-07-29'))

    # print(open_weather.return_str_weather('Чернигов'))
    # print(sinoptic.return_str_weather('Чернигов'))

    print(open_weather.return_str_weather())
    print(sinoptic.return_str_weather())
