"""Создать класс структуры данных Стек, Очередь."""

class Stack:
    def __init__(self):
        self.value = []

    def __len__(self):
        return len(self.value)

    def push(self, element):
        self.value.append(element)

    def pop(self):
        result=self.value[-1]

        #self.value = self.value[:-1]
        del(self.value[-1])
        return result

    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
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

    # el = stack1.pop()
    # print(el)
    # print(stack1)
