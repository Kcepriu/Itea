"""Создать декоратор, который будет запускать функцию в отдельном
потоке. Декоратор должен принимать следующие аргументы:
название потока, является ли поток демоном.

Создать функцию, которая будет скачивать файл из интернета по
ссылке, повесить на неё созданный декоратор. Создать список из 10
ссылок, по которым будет происходить скачивание. Создать список
потоков, отдельный поток, на каждую из ссылок. Каждый поток
должен сигнализировать, о том, что, он начал работу и по какой
ссылке он работает, так же должен сообщать когда скачивание
закончится."""

from threading import Thread
import requests


class NoLoginUser(Exception):
    pass

def downloads_threads(name_thread, type_daemon):
    def decorator(func):
        def  wrapper(*args):
            f = Thread(target=func, args=args, daemon=type_daemon, name=name_thread)
            f.start()
        return wrapper
    return decorator


@downloads_threads('test1', False)
def download_files(url):
    filename = url.split("/")[-1]
    print(f'Start downloads: {url}')

    with open(filename,"wb") as receive:
        ufr = requests.get(url)
        receive.write(ufr.content)

    print(f'Stop downloads: {url}')


urls = ['https://i-fakt.ru/wp-content/uploads/2011/05/fakty-titanik.jpg',
            'https://bigpicture.ru/wp-content/uploads/2016/04/bp11.jpg',
            'https://cs8.pikabu.ru/post_img/2018/03/18/0/1521323140119537292.jpg',
            'https://istorik.net/uploads/posts/2018-09/1537387517_titanic.jpg',
            'https://medialeaks.ru/wp-content/uploads/2019/08/titanik-fb.jpg',
            'https://24smi.org/public/media/resize/800x-/2017/8/7/01_jGxYGPs.jpg',
            'https://www.rbc.ua/static/img/_/_/____26423_650x410.jpg',
            'https://static.ukrinform.com/photos/2019_09/1567697233-112.png',
            'https://24smi.org/public/media/resize/800x-/2017/8/7/03_NZ0hk2r.jpg',
            'https://24smi.org/public/media/resize/800x-/2017/8/7/01_8fbAoD8.jpg']

for url in urls:
    download_files(url)
