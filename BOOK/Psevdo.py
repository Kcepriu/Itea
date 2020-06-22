class C1():
    def meth1(self): self.__x = 88
    def meth2(self): print(self.__x)

class C2():
    def meth1(self): self.__x = 99
    def meth2(self): print(self.__x)

class C3(C2, C1):
    pass

I = C3()

I.meth1()
I.meth2()

print(I.__dict__)