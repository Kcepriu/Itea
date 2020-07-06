# class ExamleClass:
#     def __init__(self, a):
#         self._a = a
#
#     def __call__(self, *args, **kwargs):
#         print(f'Object of class')

class Decorator:
    def __init__(self, fm):
        self.fm = fm

    def __call__(self, *args, **kwargs):
        print('Start decoration')
        dd = self.fm(*args, **kwargs)
        print('End decorartion')
        return dd

@Decorator
def target_function(arg1):
    print(arg1)
    return arg1

print(target_function(10))
# obj = ExamleClass(3)
# obj()