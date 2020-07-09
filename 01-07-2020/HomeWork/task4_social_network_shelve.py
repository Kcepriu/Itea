'''Создать подобие социальной сети. Описать классы, которые должны
выполнять соответствующие функции (Предлагаю насследовать класс
авторизации от класса регистрации). Добавить проверку на валидность
пароля (содержание символов и цифр), проверка на уникальность логина
пользователя. Человек заходит, и имеет возможность зарегистрироваться
(ввод логин, пароль, потдверждение пароля), далее входит в свою учетную
запись. Добавить возможность выхода из учетной записи, и вход в новый
аккаунт. Создать класс User, котоырй должен разделять роли обычного
пользователя и администратора. При входе под обычным пользователем мы
можем добавить новый пост, с определённым содержимим, так же пост
должен содержать дату публикации. Под учётной записью администратора
мы можем увидеть всех пользователей нашей системы, дату их регистрации,
и их посты.'''

from datetime import datetime
import re
import shelve

class NoLoginUser(Exception):
    pass

class UserLoogedIn(Exception):
    pass

class PasswordError(Exception):
    pass

class NoFindUser(Exception):
    pass

class ErrorValidationPasswords(Exception):
    pass

class UserWithLoginIsRegistered(Exception):
    pass

class UserNoAccess(Exception):
    pass

class Post:
    def __init__(self, login, text):
        self._login = login
        self._text = text
        self._date_publication = datetime.now()

    def __str__(self):
        #return f'Post:\nUser:\t{self._user.name}\nDate publication:\t{self._date_publication}\nText:\t{self._text}'
        return f'User:\t{self._login}\nDate publication:\t{self._date_publication}\nText:\t{self._text}'


class User:
    def __new__(cls, *args, **kwargs):
        #Отут треба перевірити валідність пароля і логіна
        #викликати помилку якщо не відповідають
        #помилку обробити в класі, де додаватиметься користувач
        if args and not re.match('^\w*((\d[a-z])+|([a-z]\d)+)\w*', args[2]):
            raise ErrorValidationPasswords
        return super().__new__(cls)

    def __init__(self, name, login, passwords, role):
        self._name  = name
        self._login = login
        self._passwords = passwords
        self._role = role
        self._date_registration = datetime.now()

    @property
    def name(self):
        return self._name

    def is_passwd_ok(self, password):
        #Пароль повертати мабуть не гарна ідея, краще напишу метод, який перевірятиме чи співпадають паролі
        return self._passwords == password

    @property
    def login(self):
        return self._login

    @property
    def is_admin(self):
        return self._role == 'Admin'

    def __str__(self):
        return f'Name:\t{self._name}\nLogin:\t{self._login}\nRole:\t{self._role}\nPassw:\t{self._passwords}'

class DataStorageBase:
    def __init__(self):
        self._users = {}
        self._posts = {}

    def get_user(self, login):
        return self._users.get(login)

    def add_user(self, name, login, passwords, role):
        self._users[login] = User(name, login, passwords, role)

    def add_post(self, login, text):
        posts_user=self._posts.setdefault(login, [])
        posts_user.append(Post(login, text))

    def list_logins(self, login = None):
        return filter(lambda element: True if not login else element == login, self._users.keys())

    def list_posts(self, login):
        return self._posts.get(login, [])


class DataStorage(DataStorageBase):
    def __init__(self, file_name):
        self._file_name = file_name
        with shelve.open(self._file_name) as db:
            self._users = db.get('_users', {})
            self._posts = db.get('_posts', {})

    def add_user(self, name, login, passwords, role):
        super().add_user(name, login, passwords, role)
        self.write_data('_users')

    def add_post(self, login, text):
        super().add_post(login, text)
        self.write_data('_posts')

    def write_data(self, data_name):
        with shelve.open(self._file_name) as db:
            db[data_name] = getattr(self, data_name)

class SocialNetwork():
    def __init__(self):
        self._active_user = None
        self._data_set = DataStorage('my_data')

    @property
    def is_logging(self):
        #Можна б було і не порівнювати з Ноне. Але тоді повертає всього юзера.
        return self._active_user != None

    @property
    def is_admin(self):
        return None if not self.is_logging else self._active_user.is_admin

    def registered_user(self, name, login, passwords, role):
        #реєстреватись може тільки незалогінений користувач
        #валідність пароля первірить клас юзер при додаванні
        #Треба перевірити чи не існує користувача з таким Логіном.
        if self.is_logging: raise UserLoogedIn

        if self._data_set.get_user(login): raise UserWithLoginIsRegistered

        self._data_set.add_user(name, login, passwords, role)

    def log_in(self, login, passwords):
        if  self.is_logging:
            raise UserLoogedIn

        search_user = self._data_set.get_user(login)
        if not search_user:  raise NoFindUser

        if not search_user.is_passwd_ok(passwords):  raise PasswordError

        self._active_user = search_user

    def log_off(self):
        self._active_user = None

    def add_post(self, text):
        if not self.is_logging: raise NoLoginUser
        self._data_set.add_post(self._active_user.login, text)

    def list_users(self, login=None, list_post=None):
        if not self.is_logging: raise NoLoginUser

        # Якщо не адмін не дозволяємо виводити всіх користувачів, тільки себе
        if not self.is_admin:
            if  not login:
                login = self._active_user.login
            elif login != self._active_user.login:
                raise UserNoAccess

        for element in self._data_set.list_logins(login):
            print(self._data_set.get_user(element))
            print()
            if list_post:
                self.list_posts(element)
                print()

    def list_posts(self, login):
        if not self.is_logging: raise NoLoginUser

        #Не адміну не даємо бачити пости інших користувачів
        if not self.is_admin and login != self._active_user.login:
            raise UserNoAccess

        for element in self._data_set.list_posts(login):
            print(element)
            print()

if __name__ == '__main__':
    soc_set = SocialNetwork()

    try:
        soc_set.registered_user('Serhii', 'KS', '111a111', 'Admin')
    except UserWithLoginIsRegistered:
        print(f'Пользователь KS уже зарегистрирован \n')

    try:
        soc_set.registered_user('Yura', 'yura', '111a111', 'User')
    except UserWithLoginIsRegistered:
        print(f'Пользователь yura уже зарегистрирован \n')

    #Тест 1 Спробую додати користувача з існуючим логіном
    try:
        soc_set.registered_user('DF',    'yura', '35654dd', 'User')
    except UserWithLoginIsRegistered:
        print(f'Test 1 - Пользователь yura уже зарегистрирован \n')

    #Тест 2. Не валідний пароль
    try:
        soc_set.registered_user('User1',    'user', '35654', 'User')
    except ErrorValidationPasswords:
        print(f'Test 2-1 - пароль не валидный \n')

    try:
        soc_set.registered_user('User1', 'user', 'ffffff', 'User')
    except ErrorValidationPasswords:
        print(f'Test 2-2 - пароль не валидный \n')


    # Тест 3. Заходимо з неправильним логіном
    try:
        soc_set.log_in('yura1', '111a111')
    except NoFindUser:
        print("Test 3 Не удалось войти логин неверный\n")

    # Тест 4. Заходимо з неправильним паролем
    try:
        soc_set.log_in('yura', '111a222')
    except PasswordError:
        print("Test 4 Не удалось войти пароль неверный\n")


    soc_set.log_in('yura', '111a111')

    # тест 5. Заходимо не вийшовищи
    try:
        soc_set.log_in('KS', '111a111')
    except UserLoogedIn:
        print('Test 5 Не разрешено входить сначала не разлогинившись\n')

    #Додамо декілька постів
    soc_set.add_post("Test posts 1 - yura")
    soc_set.add_post("Test posts 2 - yura")
    soc_set.add_post("Test posts 3 - yura")

    #Вивожу інфо про користувача
    print('info from user:')
    soc_set.list_users('yura')
    print()

    print('Info from user and posts:')
    soc_set.list_users('yura',True)

    #Тест 6 Хочемо побачити інформацію про іншого юзера без прав
    try:
        soc_set.list_users('KS')
    except UserNoAccess:
        print('Test 6 - Нет прав на просмотр других пользователей\n')

    #Тест 7. Хочемо побачити інформацію про всіх юзерів, не маючи прав адміна. Повинні бачити тільки себе
    soc_set.list_users()

    #Бачимо свої пости
    soc_set.list_posts('yura')

    #Test 8. Чужтх без прав адміа не бачимо
    try:
        soc_set.list_posts('KS')
    except UserNoAccess:
        print('Test 8 - Нет прав на просмотр посты других пользователей\n')

    soc_set.log_off()

    soc_set.log_in('KS', '111a111')


    soc_set.add_post("Test posts 1 - KS")
    soc_set.add_post("Test posts 2 - KS")

    soc_set.list_users(list_post=True)







