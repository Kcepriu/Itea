"""Создать класс структуры данных Стек, Очередь."""
class MyStructure()
    def __init__(self):
        self.value = []

    def __len__(self):
        return len(self.value)

    def get(self, element):
        self.value.append(element)

    def set(self, index):
        result=self.value[index]
        del(self.value[index])
        return result

    def __str__(self):
        return str(self.value)



class Queue:
    def __init__(self):
        self.value = []

    def __len__(self):
        return len(self.value)

    def enqueue(self, element):
        self.value.append(element)

    def dequeue(self):
        result=self.value[0]

        #self.value = self.value[:-1]
        del(self.value[0])
        return result

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    stack1 = Queue()

    stack1.enqueue('elem1')
    stack1.enqueue('elem2')
    stack1.enqueue('elem3')
    print(len(stack1))
    print(stack1)

    el = stack1.dequeue()
    print(el)
    print(stack1)

    el = stack1.dequeue()
    print(el)
    print(stack1)

    stack1.enqueue('elem4')
    print(stack1)

    el = stack1.dequeue()
    print(el)
    print(stack1)
