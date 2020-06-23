"""Создать декоратор с аргументами. Который будет вызывать функцию,
определенное кол-во раз, будет выводить кол-во времени
затраченного на выполнение данной функции и её название."""
import time
def repeater(repeats):
    def decorator(func):
        def wrapper(*args):
            result = []

            start_time = time.time()

            for i in range(repeats):
                # Для тесту заміру швидкодії
                time.sleep(i/10)
                result.append(func(args[0]+i, *args[1:]))

            stop_time = time.time()

            # на роботі 3.4 не підтримує такий синтаксис
            #print(f'Program runtime {stop_time-start_time} s.')
            #print(f'Function name - {func.__name__}')

            print('Program runtime %s  s.' % (stop_time-start_time))
            print('Function name - %s' % (func.__name__))

            return result
        return wrapper
    return decorator

@repeater(10)
def create_list(start, count):
    result = [i for i in range(start, start+count)]
    return result

print(create_list(2, 300))