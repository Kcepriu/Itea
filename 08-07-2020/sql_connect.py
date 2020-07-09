import sqlite3


conn = sqlite3.connect("HomeWork/students_db")
print(conn)
cursor = conn.cursor()
sql = "SELECT * FROM sqlite_sequence1"
cursor.execute(sql)

print(cursor.fetchall()) #Полная выборка по таблице or use fetchone()

conn.close()
