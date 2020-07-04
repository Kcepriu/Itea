import shelve
db = shelve.open('my_socset')

a = [1, 2, 3, 4]
dd= {'aa':[1, 2, 3], 'bb':[4, 5, 6]}
db['_users'] = a
db['_posts'] = dd
db['_users'] = dd
db.close()

db = shelve.open('my_socset')

b = db.get('_users', {})
dd1 = db.get('_posts', {})


print(b)
print(dd1)

db.close()


