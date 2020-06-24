print('Hello')
# try:
#     a = int(input('Enter a '))
#     b = int(input('Enter b '))
# except ValueError:
#    a = 0
#    b = 1

a = 1
b = 0

try:
    try:
        print(a/b)
    except ZeroDivisionError:
        print(' you cant divibe by zero! - 2')

    print('uuu')
except ZeroDivisionError:
    print(' you cant divibe by zero! -1 ')

print('world')

# try:
#     1/0
#     '123'+1
# except (ZeroDivisionError, TypeError) as err:
#     print('err')
#     pass

# try:
#     file =open('hello_file')
# except FileNotFoundError:
#     print('Не  удалось открыть файл')
# finally:
#     print('файлом окончена')
#
# file.close()