import requests
from bs4 import BeautifulSoup

class DownloadPeoples:
    def __init__(self):
        self._url = 'https://uk.wikipedia.org/w/index.php?title=Категорія:Актори_за_алфавітом'
        self.peoples = {}

    def _get_html(self, url):
        r = requests.get(url)
        return r.text

    def get_peoples(self):
        html = self._get_html(self._url)
        soup = BeautifulSoup(html, 'lxml')

        block_table_urls=soup.find('table',  class_="toc plainlinks")

        block_urls = block_table_urls.find_all('a', class_='external text')
        _urls = []
        for elem in block_urls:
            _urls.append(elem.get('href'))

        for url in _urls:
            html = self._get_html(url)
            soup = BeautifulSoup(html, 'lxml')
            block_peoples = soup.find('div', class_='mw-category')
            if not block_peoples:
                continue

            block_columns = block_peoples.find('div', class_='mw-category-group')

            blok_peopl = block_columns.find_all('a')
            try:
                for el in blok_peopl:
                    self.peoples[el.text] = 1
            except AttributeError:
                pass



dw = DownloadPeoples()
dw.get_peoples()
print(dw.peoples)