import sqlite3

class MyError(Exception):
    pass

class ErrorAutentification(MyError):
    pass

class ErrorNoFindUser(ErrorAutentification):
    pass

class ErrorWrongPassword(ErrorAutentification):
    pass

class ErrorNotLogining(ErrorAutentification):
    pass

class ErrorNotAccess(ErrorAutentification):
    pass

class NoFindId(MyError):
    pass

class UserWithLoginIsRegistered(ErrorAutentification):
    pass


class Autentification:
    def add_user(self, func, *args):
        func(*args)

    def read_data_from_user(self, func, *args):
        return func(*args)

    def update_user(self, func, *args):
        func(*args)

class Logining(Autentification):
    def __init__(self, func_read, func_write, func_update):
        self._login = None
        self._passwords = None
        self._admin = None
        self._func_read = func_read
        self._func_write = func_write
        self._func_update = func_update

    @property
    def is_admin(self):
        return self._admin

    @property
    def logged(self):
        return self._login != None

    def logout(self):
        self._login = None
        self._passwords = None
        self._admin = None

    def loggin(self, login, passwords):
        data = self.read_data_from_user(self._func_read, login)

        if not data:
            raise ErrorNoFindUser

        if data['passwords'] == passwords:
            self._login = login
            self._passwords = passwords
            self._admin = data['admin']
        else:
            raise ErrorWrongPassword

    def add_user(self, login, passwords, admin):
        if not self.logged:
            raise ErrorNotLogining

        if not self.is_admin:
            raise ErrorNotAccess

        if  self.read_data_from_user(self._func_read, login):
            raise UserWithLoginIsRegistered

        super().add_user(self._func_write, login, passwords, admin)

    def update_user(self, login, new_passorsd, new_admin):
        if not self.logged:
            raise ErrorNotLogining

        user_info = self.read_data_from_user(self._func_read, login)

        if not user_info:
            raise ErrorNoFindUser

        #якщо не адмін то може змінювати тільки свій пароль
        #Адмін може змінити як пороль так і ролдь будь кого
        if not self.is_admin:
            if self._login != login:
                raise ErrorNotAccess

            if new_admin:
                raise ErrorNotAccess

        super().update_user(self._func_update, login, new_passorsd, new_admin)


class ConnectDatabase:
    def __init__(self, name_database):
        self._name_database = name_database
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = sqlite3.connect(self._name_database)
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()
        self._conn = None
        #print('Clossing connector')

    def commit(self):
        if self._conn is None:
            raise sqlite3.DatabaseError
        self._conn.commit()
        #print('commit')

    def execute(self, sql, arg=None):
        if self._conn is None:
            raise sqlite3.DatabaseError
        if arg:
            return self._cursor.execute(sql, arg)
        else:
            return self._cursor.execute(sql)


class InitialData:
    # Отут кращеб було реалізувати через зчитування з файла. Покищо не буду замарачуватись
    # Для кожної таблиці описую як її створити, як додати в неї дані і як обновити в ній дані????
    _structure_tables = {'users': ('''CREATE TABLE users (
                            id	INTEGER PRIMARY KEY AUTOINCREMENT,
                            login	TEXT UNIQUE,
                            passwords	TEXT,
                            admin	NUMERIC DEFAULT 0)''',
                            'INSERT  INTO users (login, passwords, admin)  VALUES (?, ?, ?)',
                             ''),

                    'faculties': ('''CREATE TABLE faculties (
                                        id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name_faculty	TEXT UNIQUE)''',
                                 'INSERT INTO faculties (name_faculty)  VALUES (?)',
                             ''),

                    'gpoups': ('''CREATE TABLE gpoups (
                                    id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name_group	INTEGER UNIQUE)''',
                               'INSERT INTO gpoups (name_group)  VALUES (?)',
                             ''),

                    'students': ('''CREATE TABLE students (
                                        id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name	TEXT NOT NULL,
                                        id_faculty	INTEGER NOT NULL,
                                        id_group	INTEGER NOT NULL,
                                        student_number	INTEGER NOT NULL UNIQUE,
                                        FOREIGN KEY(id_faculty) REFERENCES facultis(id))''',
                            'INSERT INTO students (name, id_faculty, id_group, student_number)  VALUES (?, ?, ?, ?)',
                             '''UPDATE students
                                    SET name = ?, id_faculty = ?, id_group = ?, student_number = ? 
                                WHERE id = ?'''),

                    'mark_student': ('''CREATE TABLE mark_student (
                                            id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                            id_student	INTEGER NOT NULL,
                                            mark	INTEGER NOT NULL,
                                            id_item	INTEGER NOT NULL,
                                            FOREIGN KEY(id_student) REFERENCES students(id))''',
                                     'INSERT INTO mark_student (id_student, id_item, mark)  VALUES (?, ?, ?)',
                             ''),
                      'items':('''CREATE TABLE items (
                                id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                item_name	TEXT NOT NULL UNIQUE) ''',
                               'INSERT INTO items (item_name)  VALUES (?)',
                             '')   }

    _test_data ={'faculties':['Філологічний', 'Психологічний', 'Педагогічний'],

                 'gpoups':['11 группа', '22 группа', '42 группа'],

                 'items': ['История', 'Психология', 'Философия'],

                 'students':[('Петренко Петров',  ('faculties', 'name_faculty', 'Філологічний'),
                              ('gpoups', 'name_group', '11 группа'), 1256521),

                             ('Абдулова Катерина', ('faculties', 'name_faculty','Психологічний'),
                              ('gpoups', 'name_group', '42 группа'), 5555555),

                             ('Петренко Юля', ('faculties', 'name_faculty', 'Психологічний'),
                              ('gpoups', 'name_group', '42 группа'), 444444444),

                             ('Карпенко Олександр', ('faculties', 'name_faculty', 'Педагогічний'),
                              ('gpoups', 'name_group', '22 группа'), 3333333333)],

                 'mark_student':[(('students', 'student_number',  1256521), ('items', 'item_name', 'История'), 4),
                                 (('students', 'student_number',  1256521), ('items', 'item_name', 'История'), 3),
                                 (('students', 'student_number', 1256521),  ('items', 'item_name', 'Психология'), 5),
                                 (('students', 'student_number', 1256521),  ('items', 'item_name', 'Философия'), 5),
                                 (('students', 'student_number', 1256521),  ('items', 'item_name', 'Психология'), 5),

                                 (('students', 'student_number', 5555555), ('items', 'item_name', 'История'), 5),
                                 (('students', 'student_number', 5555555), ('items', 'item_name', 'История'), 5),
                                 (('students', 'student_number', 5555555), ('items', 'item_name', 'Психология'), 5),
                                 (('students', 'student_number', 5555555), ('items', 'item_name', 'Философия'), 5),
                                 (('students', 'student_number', 5555555), ('items', 'item_name', 'Психология'), 5),

                                 (('students', 'student_number', 444444444), ('items', 'item_name', 'История'), 3),
                                 (('students', 'student_number', 444444444), ('items', 'item_name', 'История'), 3),
                                 (('students', 'student_number', 444444444), ('items', 'item_name', 'Психология'), 3),
                                 (('students', 'student_number', 444444444), ('items', 'item_name', 'Философия'), 3),
                                 (('students', 'student_number', 444444444), ('items', 'item_name', 'Психология'), 3),

                                 (('students', 'student_number', 3333333333), ('items', 'item_name', 'История'), 4),
                                 (('students', 'student_number', 3333333333), ('items', 'item_name', 'История'), 4),
                                 (('students', 'student_number', 3333333333), ('items', 'item_name', 'Психология'), 5),
                                 (('students', 'student_number', 3333333333), ('items', 'item_name', 'Философия'), 4),
                                 (('students', 'student_number', 3333333333), ('items', 'item_name', 'Психология'), 5)
                                 ]
                 }

class Students:
    def __init__(self, id, name, id_faculty, id_group, student_number):
        self._id = 0
        self._name = name
        self._id_faculty = id_faculty
        self._id_group = id_group
        self._student_number = student_number

    def write_data(self, func_write):
       func_write(id=self._id, name=self._name, id_faculty=self._id_faculty,
                   id_group=self._id_group, student_number=self._student_number)

    def __str__(self):
        return f'Student name: {self._name}\n\tID faculty: {self._id_faculty}\n\tId group: {self._id_group}\n\tStudent numbers: {self._student_number}'

class DatabaseStudents(Logining, InitialData):
    def __init__(self, database_name):
        self._database_name = database_name
        super().__init__(self.read_user, self.write_user, self.update_user)
        self._curent_student = None


    def read_user(self, login):
        sql_text = 'select  id, login, passwords, admin from users where login = ?'
        result_sql = self._execute_sql(sql_text, [login])

        result = None
        if result_sql:
            result = dict(result_sql)
        # print(result)

        return result

    def write_user(self, login, passwords, admin):
        self._execute_sql(self._structure_tables['users'][1], [login, passwords, 1 if admin else 0])

    def update_user(self, login, new_passorsd, new_admin):
        #треба дописати
        print('Не реалізував')

    def _table_exists(self, table_name):
        #Перевіряю чи існує таблиця в  базі
        with ConnectDatabase(self._database_name) as connector:
            sql = "SELECT 1 FROM sqlite_master WHERE type=\'table\' and name = ?"
            try:
                cursor = connector.execute(sql, [table_name])
                return cursor.fetchall()
            except sqlite3.OperationalError:
                print('error table exists')
                pass

    def _execute_sql(self, text_sql, arg=None, commit=None, fetch_all=None):
        with ConnectDatabase(self._database_name) as connector:
            cursor = connector.execute(text_sql, arg)
            if not commit:
                connector.commit()

            return cursor.fetchall() if fetch_all else cursor.fetchone()

    def _get_id(self, table_name, field_name, value):
        sql_text = 'select id from '+table_name+' where '+field_name+' = ?'
        result = self._execute_sql(sql_text, [value])
        if result:
            return result['id']
        raise NoFindId

    def _initial_tables(self):
        #При запуску перевіримо чи існують в базі необхідні таблиці. При потребі створимо їх
        #Також внесемо двох користувачів
        for table_name, text_sql  in self._structure_tables.items():
            if not self._table_exists(table_name):
                self._execute_sql(text_sql[0])
                if table_name == 'users':
                    self._execute_sql(text_sql[1], ['admin', 'admin', 1])
                    self._execute_sql(text_sql[1], ['user', 'user', 0])

    def _fix_parametr(self, params):
        #треба для заливки текстових даних
        # Бо треба було якось вказати програмі, що деяких полів треба спочатку знайти id

        result = []
        for param in params:
            if type(param) == tuple:
                result.append(self._get_id(*param))
            else:
                result.append(param)
        return result

    def _initial_test_data(self):
        #Заллю в таблиці тестові дані
        for table_name, datas in self._test_data.items():
            for i in datas:
                try:
                    param = self._fix_parametr([*i] if type(i)==tuple else [i])
                    # print(param)
                    self._execute_sql(self._structure_tables[table_name][1], param)
                except sqlite3.IntegrityError:
                    #Помилка випадає через унікальність запису. Значить такі дані вже внесені. Ігноруємо
                    pass

    def write_student(self, **kwargs):
        print(kwargs['id'])
        if id:
            self._execute_sql(self._structure_tables['students'][1],
                              [kwargs['name'], kwargs['id_faculty'], kwargs['id_group'], kwargs['student_number']])
        else:
            self._execute_sql(self._structure_tables['students'][2],
                    [kwargs['name'], kwargs['id_faculty'], kwargs['id_group'], kwargs['student_number'], kwargs['id']])

    def add_studetn(self, name, id_faculty, id_group, student_number):
        student = Students(0, name, id_faculty, id_group, student_number)
        student.write_data(self.write_student)

if __name__ == '__main__':
    students_databases = DatabaseStudents("students_db_new.db")
    students_databases._initial_tables()
    # students_databases._initial_test_data()

    # print(students_databases._login)

    students_databases.loggin('admin', 'admin')
    # students_databases.loggin('user', 'user')
    # print(students_databases.is_admin)
    # print(students_databases.logged)
    # print(students_databases._login)
    # students_databases.logout()
    # print(students_databases.logged)
    # students_databases.add_user('ks_admin', '123456', True)

    students_databases.add_studetn('Student 1', 1, 2, 125464)




