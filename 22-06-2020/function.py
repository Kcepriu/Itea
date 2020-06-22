def a():
    print('Hello')

def b(func):
    func()

print(type(a))

b(a)

t = a
print(t.__name__)