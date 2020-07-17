import requests
import json
import datetime

class MyWeatherError(Exception):
    pass

class ErrorCityNotFound(MyWeatherError):
    pass
class ErrorInvalidApiKey(MyWeatherError):
    pass

class ErrorDate(MyWeatherError):
    pass

class ErrorFormatDate(MyWeatherError):
    pass

class OpenWeather:
    def __init__(self, api):
        self._url='http://api.openweathermap.org/data/2.5/forecast'
        self._api = api
        self._add_param= '&units=metric&lang=ru'
        self._default_city = 'Киев'

    def get_html(self, url):
        r = requests.get(url)
        return r.text

    def get_weather(self, city_name=None, date=None):
        if not city_name:
            city_name = self._default_city

        now = datetime.datetime.now()
        date = date if date else now.strftime("%Y-%m-%d")

        url=f'{self._url}?q={city_name}{self._add_param}&appid={self._api}'
        html = self.get_html(url)

        dict_weather = self.parsing_result(html)

        if not date in  dict_weather:
            raise ErrorDate

        return dict_weather[date]


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

#requests.exceptions.ConnectionError

if __name__ == '__main__':
    open_weather = OpenWeather('689b01c43ded4804a84027bf54dc0817')
    print(open_weather.get_weather('Киев','2020-07-17'))
