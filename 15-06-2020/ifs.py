import random

rn = random.randint(0, 100)

# start = 0
# end = 10000
#
# while start < end:
#     start += 1
#
#
#     if start ** 2 > 16732:
#         break
#
#     if start % 2:
#         continue
#     print(start, start ** 2)
products = {
     'cherry': 110,
     'strawberry': 100,
     'cucumber': 40
 }
for name, price in products.items():
    print(name, price)