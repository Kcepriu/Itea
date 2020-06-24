"""Создать класс
комплексного числа и реализовать для него арифметические
операции."""
class Complex:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def __str__(self):
        return ('' if self.a == 0 and self.b != 0 else str(self.a)) + \
               ('' if self.b <= 0 or self.a == 0  else '+') + ('' if self.b == 0 else  str(self.b)+'i')

    def __add__(self, other):
        return Complex(self.a + other.a,  self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return Complex(a, b)

    def __truediv__(self, other):
        z = other.a ** 2 + other.b ** 2
        a = (self.a * other.a + self.b * other.b) / z
        b = (self.b * other.a - self.a * other.b) / z
        return Complex(a, b)

    def __neg__(self):
        return Complex(-self.a , -self.b)

if __name__ == '__main__':
    n1 = Complex(-3, -5)
    print(n1)

    n2 = Complex(2, 4)
    print(n2)


    print(n1 + n2)
    print(n1 - n2)
    print(n1 * n2)
    print(n1 / n2)
    print(-n1)



