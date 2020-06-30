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

class Post:
    def __init__(self, user, text):
        self._user = user
        self._text = text
        self._date_publication = datetime.now()

    def __str__(self):
        return f'Post:\nUser:\t{self._user.name}\nDate publication:\t{self._date_publication}\nText:\t{self._text}'


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

    #Мабуть пароль повертати не сама гарна ідея. Краще перероблю в метод, який перевірятиме чи правильний пароль
    @property
    def passwords(self):
        return self._passwords

    def is_passwd_ok(self, password):
        return self._passwords == password

    @property
    def login(self):
        return self._login

    @property
    def is_admin(self):
        return self._role == 'Admin'

    def __str__(self):
        return f'Name:\t{self._name}\nLogin:\t{self._login}\nRole:\t{self._role}\nPassw:\t{self._passwords}'


class CommandLine:
    def print_help(self):
        print('\tquit')
        print('\tregistered_user(username, login, passwd, role)')
        print('\tlog_in(login, passwd)')
        print('\tlog_off()')
        print()

    def run_comman_line(self):
        while True:
            print('Enter the command')
            print('Enter help to list available commands')
            command = input('command>')

            if command == 'help':
                self.print_help()
            elif command == 'quit':
                break
            elif 'registered_user' in command:
                print('registered_user')
            else:
                print('Command error.')
                self.print_help()


class DataStorage:
    def __init__(self):
        self._users = {}
        self._posts = []

    def find_user(self, login):
        return self._users.get(login)

    def add_post(self, user, text):
        self._data_set._posts.append(Post(user, text))

class Registers:
    pass


class Login:
    pass

class SocialNetwork():
    def __init__(self):
        self._active_user = None
        self._data_set = DataStorage()
        # super(DataStorage).__init__()
        # self.run_comman_line()

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

        if self._data_set.find_user(login): raise UserWithLoginIsRegistered
        self._data_set._users[login] = User(name, login, passwords, role)

    # -
    def log_in(self, login, passwords ):
        if  self.is_logging:
            print('Вже залогінився. треба вийти')
            raise UserLoogedIn

        search_user = self._data_set.find_user(login)
        if not search_user:  raise NoFindUser
        if search_user.passwords != passwords:  raise PasswordError

        self._active_user = search_user

    # +
    def log_off(self):
        self._active_user = None

    def add_post(self, text):
        if not self.is_logging: raise NoLoginUser
        self._data_set.add_post(self._active_user, text)
        # self._data_set._posts.append(Post(self._active_user, text))


    def list_users(self, login = None):
        if not self.is_logging: raise NoLoginUser
        # search_user = self.find_user(login)
        for (login, user) in self._data_set._users.items():
            print(user)
            print()

        #Якщо ноне, то виводимо для адміна всіх, для юзера тількит активного
        #якщо логін вказано то для адміна виводимо юзера. а для юзере перевірити чи це він сам.
        #Якщо так, то виводимо інформацію про себе




if __name__ == '__main__':
    user1 = User('Serhii', 'KS', '111a111', 'Admin')
    # print(user1)
    # # print(user1._name)
    # print(user1.login)
    # print(user1.is_passwd_ok('111111') )
    #
    # post1 = Post(user1, 'text posts 1', '25-06-2020')
    #
    # print(post1)

    soc_set = SocialNetwork()
    soc_set.registered_user('Serhii', 'KS', '111a111', 'Admin')
    soc_set.registered_user('Yura', 'yura', '111a111', 'User')

    # #soc_set.log_in('KS', '111a111')
    soc_set.log_in('yura', '111a111')
    #
    print('is_logging', soc_set.is_logging)
    # print('is_admin',   soc_set.is_admin)
    #
    # soc_set.log_off()
    # print(soc_set.is_logging)

    soc_set.list_users()
    soc_set.add_post("Test posts 1")



