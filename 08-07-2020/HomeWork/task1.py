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

class NoFindObject(MyError):
    pass

class GroupDoesNotExist(MyError):
    pass

class StudetnAlreadyCreated(MyError):
    pass

class FacultiesDoesNotExist(MyError):
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

    @property
    def login(self):
        return self._login

    def logout(self):
        self._login = None
        self._passwords = None
        self._admin = None

    def loggining(self, login, passwords):
        data = self.read_data_from_user(self._func_read, login)

        if not data:
            raise ErrorNoFindUser

        if data['passwords'] == passwords:
            self._login = login
            self._passwords = passwords
            self._admin = data['admin']
        else:
            raise ErrorWrongPassword

    def access_check(self, check_admin=None):
        if not self.logged: raise ErrorNotLogining

        if check_admin:
            if not self.is_admin: raise ErrorNotAccess

    def add_user(self, login, passwords, admin):
        self.access_check(True)


        if  self.read_data_from_user(self._func_read, login):
            raise UserWithLoginIsRegistered

        super().add_user(self._func_write, login, passwords, admin)

    def update_user(self, login, new_passorsd, new_admin):
        self.access_check()

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

                    'groups': ('''CREATE TABLE groups (
                                    id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name_group	INTEGER UNIQUE)''',
                               'INSERT INTO groups (name_group)  VALUES (?)',
                             ''),

                    'students': ('''CREATE TABLE students (
                                        id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name	TEXT NOT NULL,
                                        id_faculty	INTEGER NOT NULL,
                                        id_group	INTEGER NOT NULL,
                                        student_number	INTEGER NOT NULL UNIQUE,
                                        FOREIGN KEY(id_group) REFERENCES groups(id),
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
                                            FOREIGN KEY(id_item) REFERENCES items(id),
                                            FOREIGN KEY(id_student) REFERENCES students(id))''',
                                     'INSERT INTO mark_student (id_student, id_item, mark)  VALUES (?, ?, ?)',
                             ''),
                      'items':('''CREATE TABLE items (
                                id	INTEGER PRIMARY KEY AUTOINCREMENT,
                                item_name	TEXT NOT NULL UNIQUE) ''',
                               'INSERT INTO items (item_name)  VALUES (?)',
                             '')   }
    #Для наповнення бази тестовими даними. Якби вбути впевненим що база пуста (хоча б можна було все видалити), то
    # скористатися INSERT записуючи і id. А так наробив костилів.

    _test_data ={'faculties':['Філологічний', 'Психологічний', 'Педагогічний'],

                 'groups':['11 группа', '22 группа', '42 группа'],

                 'items': ['История', 'Психология', 'Философия'],

                 'students':[('Петренко Петров',  ('faculties', 'name_faculty', 'Філологічний'),
                              ('groups', 'name_group', '11 группа'), 1256521),

                             ('Абдулова Катерина', ('faculties', 'name_faculty','Психологічний'),
                              ('groups', 'name_group', '42 группа'), 5555555),

                             ('Петренко Юля', ('faculties', 'name_faculty', 'Психологічний'),
                              ('groups', 'name_group', '42 группа'), 444444444),

                             ('Карпенко Олександр', ('faculties', 'name_faculty', 'Педагогічний'),
                              ('groups', 'name_group', '22 группа'), 3333333333)],

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


class DatabaseStudents(Logining, InitialData):
    def __init__(self, database_name):
        self._database_name = database_name
        super().__init__(self.read_user, self.write_user, self.update_user)
        self._initial_tables()

    # Функції для роботи з аутентифікацією
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

    #Функції для ініціалазіції таблиць і даних
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

    def initial_test_data(self):
        self.access_check(True)
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

    #Функції для роботи з БД
    def _execute_sql(self, text_sql, arg=None, commit=None, fetch_all=None):
        with ConnectDatabase(self._database_name) as connector:
            cursor = connector.execute(text_sql, arg)
            if commit:
                connector.commit()

            return cursor.fetchall() if fetch_all else cursor.fetchone()

    def _get_id(self, table_name, field_name, value):
        sql_text = 'select id from '+table_name+' where '+field_name+' = ?'
        result = self._execute_sql(sql_text, [value])
        if result:
            return result['id']
        raise NoFindId

    def _found_object_from_id(self, table_name, id):
       try:
           self._get_id(table_name, 'id', id)
           return True
       except NoFindId:
           return None

    #-------------------------------------------
    def write_student(self, id, name, id_faculty, id_group, student_number):
        self.access_check(True)
        if not id:
            # перевірити чи є така группа
            # перевірити чи є такий факультет
            # Перевірити чи є такий кстудени

            if self._found_object_from_id('groups', id_group):
                raise GroupDoesNotExist
            if self._found_object_from_id('faculties', id_faculty):
                raise FacultiesDoesNotExist
            try:
                self.find_student(student_number)
            except NoFindObject:
                pass
            else:
                raise StudetnAlreadyCreated

            self._execute_sql(self._structure_tables['students'][1],
                              [name, id_faculty, id_group, student_number], commit=True)
        else:
            self._execute_sql(self._structure_tables['students'][2],
                    [name, id_faculty, id_group, student_number, id], commit=True)



    def print_all_students(self):
        self.access_check()

        text_sql='select id, name from students'
        list_students = self._execute_sql(text_sql, fetch_all=True)
        print('Список студентов:')
        for student in list_students:
            print(f"{student['name']} ({student['id']})")

    def find_student(self, student_number):
        self.access_check()
        text_sql = 'select id, name from students where student_number = ?'

        student = self._execute_sql(text_sql, [student_number])
        if not student:
            raise NoFindObject

        return student


    def print_student_find_number(self, student_number):
        self.access_check()
        text_sql = 'select id, name from students where student_number = ?'
        try:
            student = self.find_student(student_number)
            print(f'Студент №{student_number} ', f"{student['name']} ({student['id']})")
        except NoFindObject:
            print(f'Студента №{student_number} не знайдено')


    def print_mark_student(self, student_id):
        self.access_check()
        text_sql='''select  it.item_name, m.mark from mark_student m
                    INNER JOIN items it
                    ON m.id_item = it.id
                    where m.id_student = ?
                    order by it.item_name'''
        mark_student = self._execute_sql(text_sql, [student_id], fetch_all=True)

        print('Оцінки студента:')
        for mark in mark_student:
            print(f"\t{mark['item_name']} {mark['mark']}")

    def print_info_current_student(self, student_id):
        self.access_check()
        text_sql = '''select st.name, st.student_number, gr.name_group, fc.name_faculty    
                    from students st
                    INNER JOIN groups gr, faculties fc
                    ON st.id_group = gr.id and st.id_faculty=fc.id
                    where st.id = ?'''

        student = self._execute_sql(text_sql, [student_id])
        if not student:
            raise NoFindId
        print(f"Студент: {student['name']}\n\t№ студенського: {student['student_number']}\n\tГрупа: {student['name_group']}\n\tФакультет: {student['name_faculty']}")

    def print_students_avg_mark(self, avg_mark):
        self.access_check()
        text_sql = '''select st.id, st.name, av.avg_mark from students st
                        INNER JOIN
                        (select id_student, avg(mark) avg_mark from mark_student group by id_student HAVING avg(mark) >= ?) av
                        on st.id=av.id_student'''

        students = self._execute_sql(text_sql, [avg_mark], fetch_all=True)

        print(f'Студенты с средним балом большим {avg_mark}:')
        for student in students:
            print(f"\t{student['name']} - {student['avg_mark']}  ({student['id']})")

    def print_groups(self):
        self.access_check()
        text_sql = 'select id, name_group from groups'

        groups = self._execute_sql(text_sql, fetch_all=True)

        print(f'Список груп:')
        for group in groups:
            print(f"\t{group['name_group']}  ({group['id']})")

    def print_faculties(self):
        self.access_check()
        text_sql = 'select id, name_faculty from faculties'

        faculties = self._execute_sql(text_sql, fetch_all=True)

        print(f'Список факультетів:')
        for facult in faculties:
            print(f"\t{facult['name_faculty']}  ({facult['id']})")



class Menu:
    #Примітивніше меню. Поки не готовий написати щось краще
    def __init__(self):
        self._students_databases = DatabaseStudents("students_db_new.db")
        self.init_menu()
        self.work()

    def init_menu(self):
        self.menu = {'1': 'Залогинится',
                '2':'Разлогиниться',
                '3':'Заповнити тестовими даними',
                '4':'Додати користувача',
                '5': 'Змінити пароль',
                '6': 'Додати студента',
                '7': 'Змінити студента',
                '8': 'Вивести список всіх студентів',
                '9': 'Висести список відмінників',
                '10': 'Шукати студента по номеру студентського квитка',
                '11': 'Інформація про студента',
                'q': 'Вийти з программи'
                }

    def print_command(self):
        print()
        for command, text in self.menu.items():
            print(f"\t{command} - {text}")

    def work(self):
        while True:
            add_role = ' (adm)' if self._students_databases.is_admin else ' (usr)'
            add_login = ' ' + self._students_databases.login+add_role if self._students_databases.logged else ''
            self.print_command()
            command = input('Ведите команду'+add_login+': ')
            if command == 'q':
                print(f'\nДо побачення\n')
                break
            elif not command in self.menu:
                print(f'\nНе вірна комманда\n')
            else:
                func = getattr(self, 'command'+str(command), None)
                if func:
                    func()

    def run_command(self, comman):
        print(self.menu[command])

    def command1(self):
        login = input('Введіть логін: ')
        passwd = input('Введіть пароль: ')

        try:
            self._students_databases.loggining(login, passwd)
        except ErrorNoFindUser:
            print('Не вірний логін')
        except ErrorWrongPassword:
            print('Не вірний пароль')
        else:
            print('Вітаємо')

    def command2(self):
        self._students_databases.logout()

    def command3(self):
        try:
            self._students_databases.initial_test_data()
        except ErrorNotLogining:
            print('Спочатку треба залогінитись')
        except ErrorNotAccess:
            print('Нема доступу')




    def command4(self):
        print('Не реализовано')

    def command5(self):
        print('Не реализовано')

    def command6(self):
        try:
            self._students_databases.access_check(True)
            name = input('Введіть ФІО студента: ')
            self._students_databases.print_groups()
            id_group = input('Введіть ID групи: ')
            self._students_databases.print_faculties()
            id_faculty = input('Введіть ID групи: ')
            student_number = input('Введіть № студентського: ')

            self._students_databases.write_student(0, name, id_faculty, id_group, student_number)

        except ErrorNotLogining:
            print('Спочатку треба залогінитись')
        except ErrorNotAccess:
            print('Нема доступу')
        except sqlite3.OperationalError:
            print('Не вдалося записати дані')
        except GroupDoesNotExist:
            print('Не вірно вказано номер групи')
        except FacultiesDoesNotExist:
            print('Не вірно вказано номер факультету')
        except StudetnAlreadyCreated:
            print('Студент з таким номером студентського вже існує')
        else:
            print('Студента додано')

    def command7(self):
        print('Не реализовано')

    def command8(self):
        try:
            self._students_databases.print_all_students()
        except ErrorNotLogining:
            print('Спочатку треба залогінитись')

    def command9(self):
        try:
            self._students_databases.print_students_avg_mark(4.5)
        except ErrorNotLogining:
            print('Спочатку треба залогінитись')

    def command10(self):
        student_number = input('Введіть номер студентського: ')
        try:
            self._students_databases.print_student_find_number(student_number)
        except ErrorNotLogining:
            print('Спочатку треба залогінитись')
        except NoFindId:
            print('Студента не знайдено')

    def command11(self):
        id = input('Введіть id студента: ')
        try:
            self._students_databases.print_info_current_student(id)
        except ErrorNotLogining:
            print('Спочатку треба залогінитись')
        except NoFindId:
            print('Студента не знайдено')

if __name__ == '__main__':
    menu=Menu()

    # students_databases = DatabaseStudents("students_db_new.db")
    # students_databases._initial_tables()
    # # students_databases._initial_test_data()
    #
    # # print(students_databases._login)
    #
    # students_databases.loggin('admin', 'admin')
    # # students_databases.loggin('user', 'user')
    # #
    # # # students_databases.add_user('ks_admin', '123456', True)
    # #
    # # # students_databases.add_studetn('Student 1', 1, 2, 125464)
    # # students_databases.print_all_students()
    # #
    # students_databases.print_student_find_number(333)
    # students_databases.print_student_find_number(5555555)
    # print()
    # students_databases.print_info_current_student(2)
    # students_databases.print_mark_student(2)
    # students_databases.print_students_avg_mark(4.2)



