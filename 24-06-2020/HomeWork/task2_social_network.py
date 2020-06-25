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

class NoLoginUser(Exception):
    pass

class UserLoogedIn(Exception):
    pass

class PasswordError(Exception):
    pass

class NoFindUser(Exception):
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
        pass

    def __init__(self, name, login, passwords, role):
        self._name = name
        self._login = login
        self._passwords = passwords
        self._role = role
        self._date_registration = datetime.now()

    @property
    def name(self):
        return self._name

    @property
    def passwords(self):
        return self._passwords

    @property
    def login(self):
        return self._login

    @property
    def is_admin(self):
        return self._role == 'Admin'

class SocialNetwork:
    def __init__(self):
        self._users = {}
        self._posts = []
        self._active_user = None

    def find_user(self, login):
        return self._users.get(login)

    def is_logging(self):
        return self._active_user

    def is_admin(self):
        if not self.is_logging(): return None
        return self._active_user

    # зараз отут
    def registered_user(self, name, login, passwords, role):
        #реєстреватись може тільки незалогінений користувач
        #валідність пароля первірить клас юзер при додаванні
        #Треба перевірити чи не існує користувача з таким паролем.
        if is_logging(self): raise NoLoginUser

        self._users[login] = User(name, login, passwords, role)


    def login(self, login, passwords ):
        if  is_logging(self):
            print('Вже залогінився. треба вийти')
            raise UserLoogedIn

        search_user = self.find_user(login)
        if not search_user:  raise NoFindUser
        if search_user.passwords != passwords:  raise PasswordError

        self._active_user = search_user

    def logoff(self):
        self._active_user = None

    def add_post(self, text):
        if not is_logging(self): raise NoLoginUser

        self._posts.append(Post(self._active_user, text))

    def list_users(self, login = None):
        if not is_logging(self): raise NoLoginUser


        search_user = self.find_user(login)


        #Якщо ноне, то виводимо для адміна всіх, для юзера тількит активного
        #якщо логін вказано то для адміна виводимо юзера. а для юзере перевірити чи це він сам.
        #Якщо так, то виводимо інформацію про себе




if __name__ == '__main__':

    user1 = User('Serhii', 'KS', '111111', 'admin')

    post1 = Post(user1, 'text posts 1', '25-06-2020')

    #print(post1)
