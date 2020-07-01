squares = [i**2 for i in range(10) if i%2 == 0]
squares = [i**3 if i % 2 == 0 else i ** 2 for i in range(10) ]

print(squares)

compr_dic = {i: i **2 for i in range(10)}
print(compr_dic)

compr_set = {i for i in range(10)}

print(compr_set)