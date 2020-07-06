cars = ['BMW', 'Audi', 'VW']

# for car in cars:
#     print(car)

# car_iter = cars.__iter__()
# print(car_iter.__next__())
# print(car_iter.__next__())
#
#
# print(car_iter.__next__())
# print(car_iter.__next__())

car_iter = iter(cars)
print(next(car_iter))
print(next(car_iter))
print(next(car_iter))
print(next(car_iter))