import sqlite3

class Logining:
    def __init__(self):
        self._login = None
        self._passwords = None
        self._loginnin = None

    def loggin(self, login, passwords):
        self._login = login
        self._passwords = passwords

class ConnectDatabase:
    def __init__(self, name_database):
        self._name_database = name_database
        self._connect = None

    def __enter__(self):
        try:
            conn = sqlite3.connect(self._name_database)
            self._cursor = conn.cursor()
            self._connect = True
        except sqlite3.Error:
            raise sqlite3.C


conn = sqlite3.connect("students_db")
cursor = conn.cursor()
sql = "SELECT * FROM users "
cursor.execute(sql)
print(cursor.fetchall()) #Полная выборка по таблице or use fetchone()
