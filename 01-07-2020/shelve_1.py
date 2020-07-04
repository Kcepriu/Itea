import shelve
db = shelve.open('my_socset')

a = [1, 2, 3, 4]
db['a'] = a
db.close()

db = shelve.open('my_socset')

b = db['a']

print(b)

db.close()
