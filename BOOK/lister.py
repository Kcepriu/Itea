class ListInstance():
    def __str__(self):
        return '<Instance of %s, adress %s \n%s>' % (
                                    self.__class__.__name__,
                                    id(self),
                                    self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result

class testt(ListInstance):
    s = 10
    dd = 20
    def test_def(self): pass

I = testt()
I.a=10


print(I)

print(dir(object))