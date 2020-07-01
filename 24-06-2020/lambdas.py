# def to_square(num):
#     return num ** 2
#

# to_squard_lambda = lambda num: num ** 2
#
# print(to_squard_lambda(2))

# 2

# def confirm_function(func, arg):
#     return func(arg)
#
# print(confirm_function(lambda num: num ** 2, 4))

# 3
# def to_square(num):
#      return num ** 2
# result = map(to_square, [1, 2, 3, 4, 5])
#
# print(list(result))

# 4
# result = map(lambda num: num ** 2, [1, 2, 3, 4, 5, 6])
# print(list(result))

# 5
# result = map(lambda num1, num2: (num1 ** 2, num2 ** 2), [1, 2, 3, 4, 5, 6], [10, 20, 30, 40, 50])
# print(list(result))

# 6
# result = filter(lambda number: number > 100, [10, 200, 101, 302, 16])
# print(list(result))

# error
# result = filter(number > 100, [10, 200, 101, 302, 16])
# print(list(result))


dd = {'as':1234, 'sd':2345, 'df': 3456}
# print(dd)
result = filter(lambda login: login[0] == 'as', dd.items() )


print(list(result))

# a = 100
