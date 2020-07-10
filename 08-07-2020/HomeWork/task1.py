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


class Autentification:
    def add_user(self, func, *args):
        func(*args)

    def read_data_from_user(self, func, *args):
        return func(*args)


class Logining(Autentification):
    def __init__(self, func_read, func_write):
        self._login = None
        self._passwords = None
        self._admin = None
        self._func_read = func_read
        self._func_write = func_write

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

        if data.passwords == passwords:
            self._login = login
            self._passwords = passwords
            self._admin = data.admin
        else:
            raise ErrorWrongPassword


    def add_user(self, login, passwords, admin):
        if not self.logged:
            raise ErrorNotLogining
        if not self.is_admin:
            raise ErrorNotAccess

        super().add_user(self._func_write, login, passwords, admin)


class ConnectDatabase:
    def __init__(self, name_database):
        self._name_database = name_database
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = sqlite3.connect(self._name_database)
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
                            'INSERT  INTO users (login, passwords, admin)  VALUES (?, ?, ?)'),

                    'faculties': ('''CREATE TABLE faculties (
                                        id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name_faculty	TEXT UNIQUE)''',
                                 'INSERT INTO faculties (name_faculty)  VALUES (?)'),

                    'gpoups': ('''CREATE TABLE gpoups (
                                    id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name_group	INTEGER UNIQUE)''',
                               'INSERT INTO gpoups (name_group)  VALUES (?)'),

                    'students': ('''CREATE TABLE students (
                                        id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name	TEXT NOT NULL,
                                        id_faculty	INTEGER NOT NULL,
                                        id_group	INTEGER NOT NULL,
                                        student_number	INTEGER NOT NULL UNIQUE,
                                        FOREIGN KEY(id_faculty) REFERENCES facultis(id))''',
                            'INSERT INTO students (name, id_faculty, id_group, student_number)  VALUES (?, ?, ?, ?)'),

                    'mark_student': ('''CREATE TABLE mark_student (
                                            id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                            id_student	INTEGER NOT NULL,
                                            mark	INTEGER NOT NULL,
                                            id_item	TINTEGER NOT NULL,
                                            FOREIGN KEY(id_student) REFERENCES students(id))''',
                                     'INSERT INTO mark_student (id_student, item_name, mark)  VALUES (?, ?, ?)'),
                      'items':('''CREATE TABLE items (
                                id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                items	TEXT NOT NULL)''',
                               'INSERT INTO items (item_name)  VALUES (?)')   }

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
                              ('gpoups', 'name_group', '22 группа'), 3333333333)]
        # ,
        #
        #          'mark_student':[(('students', 'student_number',  1256521), 'Математика', 4),
        #                          (('students', 'student_number',  1256521), 'Математика', 3),
        #                          (('students', 'student_number', 1256521), 'Математика', 5),
        #                          (('students', 'student_number', 1256521), 'Фізика', 5),
        #                          (('students', 'student_number', 1256521), 'Математика', 5),
        #                          ]
                 }



class DatabaseStudents(Logining, InitialData):
    def __init__(self, database_name):
        self._database_name = database_name

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

    def _execute_sql(self, text_sql, arg=None, commit=None):
        with ConnectDatabase(self._database_name) as connector:
            cursor = connector.execute(text_sql, arg)
            if not commit:
                connector.commit()

            return cursor.fetchall()

    def _get_id(self, table_name, field_name, value):
        sql_text = 'select id from '+table_name+' where '+field_name+' = ?'
        result = self._execute_sql(sql_text, [value])
        if result:
            return result[0][0]

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
        result = []
        for param in params:
            if type(param) == tuple:
                result.append(self._get_id(*param))
            else:
                result.append(param)
        return result

    def _initial_test_data(self):
        for table_name, datas in self._test_data.items():
            for i in datas:
                try:
                    param = self._fix_parametr([*i] if type(i)==tuple else [i])
                    # print(param)
                    self._execute_sql(self._structure_tables[table_name][1], param )
                except sqlite3.IntegrityError:
                    #Помилка випадає через унікальність запису. Значить таці дані вже внесені
                    pass

if __name__ == '__main__':
    students_databases = DatabaseStudents("students_db_new.db")
    students_databases._initial_tables()
    students_databases._initial_test_data()

