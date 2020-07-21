class Test:
    dd = ''
    count = 0
    def __init__(self):
        self.dd = 'TEST1'

    def __get__(self, instance, owner):
        self.count += 1



print(Test().dd)
print(Test().dd)
print(Test().count)