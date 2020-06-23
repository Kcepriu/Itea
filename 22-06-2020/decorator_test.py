def repeater(repeats):

    def decorator(func):
        print('decorator')
        print(func)
        print(func.__name__)

        def wrapper(*arg):
            i = 1
            print('i = ', i)
            i += 1
            print('Function is wrapping')
            print('Function id wrapped')

        return wrapper
    return decorator

@repeater(1)
def hello_f():
    print('Hello world')


print('Run 1')
hello_f()

print('Run 2')
hello_f()

