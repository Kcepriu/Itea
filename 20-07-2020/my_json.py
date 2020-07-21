import json

cart = {
    'strawberry': {
        'quantity':3,
        'total_price':100
    },
    'tomato': {
        'quantity':1,
        'total_price':20
    },
    'is_paid' : True,
    'distinct_product': ['strawberry', 'tomato']


}

res = json.dumps(cart)
print(res)

#####################

new_cart = json.loads(res)

print(type(new_cart))
print(new_cart)