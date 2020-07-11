def test(**kwargs):
    print(kwargs.get('id', 0))


test(dd=1, id1=10)