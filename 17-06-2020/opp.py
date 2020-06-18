class Cat:
    famely ='111'
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender



    def say_meow(self):
        print('Meeooow!', self.name)

    def __str__(self):
        return self.name+" "+self.gender


cat = Cat('jony', 'male')
cat1 = Cat(gender = 'female', name = 'Tom')

print(cat1.name)
print(cat.gender)

cat.say_meow()

print(cat1)

print(cat.famely)
Cat.famely = 'dd'


print(cat.famely)

print(cat1.famely)