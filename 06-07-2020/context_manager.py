class MyContextManager:
    def __init__(self, *args):
        self.args = args
        self.status = 1
        self.errors_texts_lists = []

    def __enter__(self):
        print('Enter CM')
        if self.status == 1:
            return self
        raise ValueError('Object cannot be used')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        if exc_type == TypeError:
            self.errors_texts_lists.append(exc_val)
            print('U did someth')

        print('CM exited')
        self.status = 0

with MyContextManager(1, 2, 3, 4, 5, 100) as my_cm:
    print(my_cm.status)
    my_cm.args[0] = 1
    print(my_cm.args)

print(my_cm.status)



