import random

def repeater(repeats):

    def decarator(func):

        def wrapper(*args):
            print('Function is wrapping')
            resunts = []
            for i in range(repeats):
                resunts.append(func(*args))

            print('Function id wrapped')
            return  resunts
        return wrapper
    return decarator

def hello():
    print('Hello word')

# @decarator
# def get_pi():
#     return 3.1415

#@decarator
#@repeater(10)
def get_random(min_, max_):
    return random.randint(min_, max_)


# wrapper_obj = decarator(get_pi)
# r = wrapper_obj()
#
# print(r)

# print(get_pi())

print(get_random(10, 20))

#print(decarator(get_random)(100))
print(repeater(30)(get_random)(10, 300))