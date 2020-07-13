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