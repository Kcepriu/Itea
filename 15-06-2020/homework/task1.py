"""1)Создать список из N элементов (от 0 до n с шагом 1). В этом списке вывести все четные значения."""
n = int(input())

res = list(range(n+1))
for i in res:
    if not i % 2:
        print(i)

