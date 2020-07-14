import sqlite3
from queries import QueryFromTables

class ConnectDatabase():
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

class Databases(QueryFromTables):
    def __init__(self, name_database):
        self._name_database = name_database
        super().__init__()
        self.initial_tables()

    def execute_sql(self, text_sql, arg=None, commit=None, fetch_all=None):
        with ConnectDatabase(self._name_database) as connector:
            cursor = connector.execute(text_sql, arg)
            if commit:
                connector.commit()

            return cursor.fetchall() if fetch_all else cursor.fetchone()

    def _table_exists(self, table_name):
        # Перевіряю чи існує таблиця в  базі
        with ConnectDatabase(self._name_database) as connector:
            sql = "SELECT 1 FROM sqlite_master WHERE type=\'table\' and name = ?"
            try:
                cursor = connector.execute(sql, [table_name])
                return cursor.fetchall()
            except sqlite3.OperationalError:
                pass

    def initial_tables(self):
        #При запуску перевіримо чи існують в базі необхідні таблиці. При потребі створимо їх
        create_tables = None
        for table_name, text_sql  in self.query_create_tables.items():
            if not self._table_exists(table_name):
                self.execute_sql(text_sql, commit=True)
                create_tables = True

        if create_tables:
            self.initial_test_data()

    def count_rows(self, table_name):
        text_sql = 'select count(id) count from '+table_name
        result = self.execute_sql(text_sql)
        return result['count'] if result else 0

    def initial_test_data(self):
        if not self.count_rows('categories'):
            for text_sql in self.query_test_data():
                self.execute_sql(text_sql, commit=True)

