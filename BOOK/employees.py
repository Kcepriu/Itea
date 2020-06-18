class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary*(1+percent)
    def work(self):
        print(self.name, "does stuff")
    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 5000)
    def work(self):
        print(self.name, "makes food")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 4000)
    def work(self):
        print(self.name, 'interfaces with customer')

class PizzaRobot(Chef):
    def work(self):
        print(self.name, "makes pizza")

if __name__ == '__main__':
    bob = PizzaRobot('bob')
    print(bob)

    bob.work()
    bob.giveRaise(0.2)
    print(bob)
    print()

    for klass in (Employee, Chef, Server, PizzaRobot):
        obj = klass(klass.__name__)
        obj.work()


