'''3) Написать свой контекстный менеджер для работы с файлами.'''

class MyConnect:
    def __init__(self, url, port):
        self._url = url
        self._port = port

    def __enter__(self):
        print(f'Connecting {self._url}:{self._port}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Disconect from  {self._url}:{self._port}')
        if exc_type is None:
            print('exited normaly')
        else:
            print('error read data', exc_type)
    def read_data(self):
        return 'data'

with MyConnect('site.com', 5060) as connect:
    print(connect.read_data())
    print(connect.read_data())
    raise EOFError
    print(connect.read_data())







