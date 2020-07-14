import requests
import json
#http://api.openweathermap.org/data/2.5/forecast?q=козелец&units=metric&lang=ru&appid=689b01c43ded4804a84027bf54dc0817
class OpenWeather:
    def __init__(self, api):
        self._url='http://api.openweathermap.org/data/2.5/forecast'
        self._api = api
        self._add_param= '&units=metric&lang=ru'

    def get_html(self, url):
        r = requests.get(url)
        return r.text

    def get_weather(self, city_name=None):
        if not city_name:
            city_name = self._default_city
        url=f'{self._url}?q={city_name}{self._add_param}&appid={self._api}'
        return self.get_html(url)

    def parsing_result(self, text):
        dict_result = json.loads(text)
        pass

#requests.exceptions.ConnectionError

if __name__ == '__main__':
    open_weather = OpenWeather('689b01c43ded4804a84027bf54dc0817')
    html = open_weather.get_weather('Киев')
    result = json.loads(html)
    print(result)
    print(result['cod'])
