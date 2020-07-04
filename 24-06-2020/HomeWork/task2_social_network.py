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
    def __init__(self, user, text):
        self._user = user
        self._text = text
        self._date_publication = datetime.now()

    def __str__(self):
        #return f'Post:\nUser:\t{self._user.name}\nDate publication:\t{self._date_publication}\nText:\t{self._text}'
        return f'User:\t{self._user.name}\nDate publication:\t{self._date_publication}\nText:\t{self._text}'


class User:
    def __new__(cls, *args, **kwargs):
        #Отут треба перевірити валідність пароля і логіна
        #викликати помилку якщо не відповідають
        #помилку обробити в класі, де додаватиметься користувач
        #print(args[0])
        if not re.match('^\w*((\d[a-z])+|([a-z]\d)+)\w*', args[2]):
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
    def __init__(self, data_from_disk):
        self._users = {}
        self._posts = {}


class DataStorage:
    def __init__(self):
        self._users = {}
        self._posts = {}

    def get_user(self, login):
        return self._users.get(login)

    def add_user(self, name, login, passwords, role):
        self._users[login] = User(name, login, passwords, role)

    def add_post(self, user, text):
        posts_user=self._posts.setdefault(user, [])
        posts_user.append(Post(user, text))

    def list_logins(self, login = None):
        return filter(lambda element: True if not login else element == login, self._users.keys())

    def list_posts(self, user):
        return self._posts.get(user, [])


class SocialNetwork():
    def __init__(self):
        self._active_user = None
        self._data_set = DataStorage()

    @property
    def is_logging(self):
        #Можна б було і не порівнювати з Ноне. Але тоді повертає всього юзера.
        return self._active_user != None

    @property
    def is_admin(self):
        return None if not self.is_logging else self._active_user.is_admin

    # -
    def registered_user(self, name, login, passwords, role):
        #реєстреватись може тільки незалогінений користувач
        #валідність пароля первірить клас юзер при додаванні
        #Треба перевірити чи не існує користувача з таким Логіном.
        if self.is_logging: raise UserLoogedIn

        if self._data_set.get_user(login): raise UserWithLoginIsRegistered

        self._data_set.add_user(name, login, passwords, role)

    # -
    def log_in(self, login, passwords):
        if  self.is_logging:
            print('Вже залогінився. треба вийти')
            raise UserLoogedIn

        search_user = self._data_set.get_user(login)
        if not search_user:  raise NoFindUser

        if not search_user.is_passwd_ok(passwords):  raise PasswordError

        self._active_user = search_user

    # +
    def log_off(self):
        self._active_user = None

    def add_post(self, text):
        if not self.is_logging: raise NoLoginUser
        self._data_set.add_post(self._active_user, text)

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

        for element in self._data_set.list_posts(self._data_set.get_user(login)):
            print(element)
            print()

if __name__ == '__main__':
    soc_set = SocialNetwork()
    soc_set.registered_user('Serhii', 'KS', '111a111', 'Admin')
    soc_set.registered_user('Yura', 'yura', '111a111', 'User')

    #Тест 1 Спробую додати користувача з існуючим логіном
    #soc_set.registered_user('DF',    'yura', '35654dd', 'User')

    #Тест 2. Не валідний пароль
    # soc_set.registered_user('User1',    'user', '35654', 'User')
    # soc_set.registered_user('User1', 'user', 'ffffff', 'User')

    # Тест 3. Заходимо з неправильним логіном
    # soc_set.log_in('yura1', '111a111')

    # Тест 4. Заходимо з неправильним паролем
    #soc_set.log_in('yura', '111a222')

    soc_set.log_in('yura', '111a111')
    soc_set.add_post("Test posts 1 - yura")
    soc_set.add_post("Test posts 2 - yura")
    soc_set.add_post("Test posts 3 - yura")


    # тест 5. Заходимо не вийшовищи
    #soc_set.log_in('KS', '111a111')

    soc_set.list_users('yura')
    soc_set.list_users('yura',True)

    #Тест 6 Хочемо побачити інформацію про іншого юзера без прав
    # soc_set.list_users('KS')

    #Тест 7. Хочемо побачити інформацію про всіх юзерів, не маючи прав адміна. Повинні бачити тільки себе
    soc_set.list_users()

    #Бачимо свої пости
    soc_set.list_posts('yura')

    #Test 8. Чужтх без прав адміа не бачимо
    #soc_set.list_posts('KS')

    soc_set.log_off()

    soc_set.log_in('KS', '111a111')


    soc_set.add_post("Test posts 1 - KS")
    soc_set.add_post("Test posts 2 - KS")

    soc_set.list_users()







