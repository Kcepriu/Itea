def my_range(start, stop, end = 1):
    while start <stop:
        value = start
        start +=1
        yield value
        print('Unforozed')
        yield 1000

# print(next(my_range(1, 100)))
# print(list(my_range(1, 100)))

# for i in my_range(1, 100):
#     print(i)

my_iter = iter(my_range(1, 3))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
