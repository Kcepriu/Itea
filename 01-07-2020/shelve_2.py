import shelve
from datetime import datetime

class User:
    def __init__(self, name, login, passwords, role):
        self._name  = name
        self._login = login
        self._passwords = passwords
        self._role = role
        self._date_registration = datetime.now()


users = {'KS':User('Serhii', 'KS', '111a111', 'Admin'), 'yura':User('Yura', 'yura', '111a111', 'User')}

print(users)

with shelve.open('my_socset') as db:
    db['users'] = users

with shelve.open('my_socset') as db:
    print(db.keys())
    new_users = db.get('users')

print(new_users)