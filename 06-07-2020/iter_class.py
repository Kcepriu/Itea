class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start<self.end:
            value = self.start
            self.start += self.step
            return value
        else:
            raise StopIteration

my_range = MyRange(0, 5, 1)

# iter_my_range = iter(my_range)
# print(next(iter_my_range))
# print(next(iter_my_range))
# print(next(iter_my_range))
# print(next(iter_my_range))
# print(next(iter_my_range))
# print(next(iter_my_range))

# for i in my_range:
#     print(i)

print(list(my_range))
