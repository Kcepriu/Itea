class Balloon:
    def __init__(self, size, colour):
        self.size = size
        self.colour = colour

    def fly(self):
        print(f'The ballon of {self.colour} is flying')

    def __add__(self, other):
        size =  self.size = other.size
        colour = self.colour + '-' + other.colour
        return Balloon(size, colour)




balloon = Balloon(10, 'red')
balloon1 = Balloon(15, 'gren')
balloon2 = Balloon(20, 'blue')
balloon.fly()
balloon1.fly()
balloon3  = balloon + balloon1 + balloon2
balloon3.fly()
print(balloon3)