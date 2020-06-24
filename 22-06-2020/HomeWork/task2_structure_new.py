class Stack(list):
    def push(self, element):
        super().append(element)

    def pop(self):
       return super().pop()

class Queue(list):
    def enqueue(self, element):
        super().append(element)

    def dequeue(self):
        return super().pop(0)




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



