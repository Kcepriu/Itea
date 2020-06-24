"""Создать класс структуры данных Стек, Очередь."""
class MyStructure:
    def __init__(self):
        self.value = []

    def __len__(self):
        return len(self.value)

    def get_element(self, element):
        self.value.append(element)

    def set_element(self, index):
        result=self.value[index]
        del(self.value[index])
        return result

    def __str__(self):
        return str(self.value)


class Queue(MyStructure):
    def enqueue(self, element):
        super().get_element(element)

    def dequeue(self):
        return super().set_element(0)


class Stack(MyStructure):
    def push(self, element):
        super().get_element(element)

    def pop(self):
       return super().set_element(-1)


if __name__ == '__main__':
    print('-'*20)
    print('Test Stack')

    stack1 = Stack()

    stack1.push('elem1')
    stack1.push('elem2')
    stack1.push('elem3')
    print(len(stack1))
    print(stack1)

    el = stack1.pop()
    print(el)
    print(stack1)

    el = stack1.pop()
    print(el)
    print(stack1)

    stack1.push('elem4')
    print(stack1)

    el = stack1.pop()
    print(el)
    print(stack1)


    print('-'*20)
    print('Test Queue')

    queue = Queue()

    queue.enqueue('elem1')
    queue.enqueue('elem2')
    queue.enqueue('elem3')
    print(len(queue))
    print(queue)

    el = queue.dequeue()
    print(el)
    print(queue)

    el = queue.dequeue()
    print(el)
    print(queue)

    queue.enqueue('elem4')
    print(queue)

    el = queue.dequeue()
    print(el)
    print(queue)
