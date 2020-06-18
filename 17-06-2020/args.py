def my_sum(*args):
    result = 0
    for number in args:
        result += number

    return result
arg1 = [1, 2, 3, 4]
arg2 = [5, 6]
r = my_sum(*arg1, *arg2)
print(r)

