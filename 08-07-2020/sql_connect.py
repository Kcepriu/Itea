import sqlite3


conn = sqlite3.connect("HomeWork/students_db")
print(conn)
cursor = conn.cursor()
sql = "SELECT * FROM users "
cursor.execute(sql)
conn.close()
print(cursor.fetchall()) #Полная выборка по таблице or use fetchone()
