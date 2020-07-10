import sqlite3


conn = sqlite3.connect("HomeWork/students_db_new.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()
sql = "SELECT * FROM users where id = 1"
cursor.execute(sql)
#print(cursor.rowcount)
# print(cursor.fetchall())

#
#
# for i in cursor.fetchall():
#     print(i['login'], i['passwords'])

dd = cursor.fetchone()
if dd:
    print(dict(dd))

# print(dd)
# print(cursor.fetchone())

conn.close()
