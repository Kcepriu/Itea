import sqlite3


conn = sqlite3.connect("HomeWork/students_db_new.db")
print(conn)
cursor = conn.cursor()
sql = "SELECT * FROM ?"
cursor.execute(sql, ['faculties'])

print(cursor.fetchall()) #Полная выборка по таблице or use fetchone()

conn.close()
