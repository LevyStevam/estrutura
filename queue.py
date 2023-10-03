from node import Node

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.len = 0

    def is_empty(self):
        return self.front is None

    def enQueue(self, data):
        temp = Node(data)

        if self.rear is None:
            self.front = self.rear = temp
            return

        self.rear.next = temp
        self.rear = temp
        self.len += 1

    def deQueue(self):
        if self.is_empty():
            return

        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None

        self.len -=1
        return temp.data
    
    def returnRear(self):
        return self.rear

    def returnRear(self):
        return self.front
    def returnLen(self):
        return self.len
pilha = Queue()
pilha.enQueue(13)
pilha.enQueue(16)
pilha.enQueue(18)
print(pilha.deQueue())
print(pilha.deQueue())
print(pilha.returnLen())
class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.len = 0

    def is_empty(self):
        return self.front is None

    def enQueue(self, data):
        temp = Node(data)

        if self.rear is None:
            self.front = self.rear = temp
            self.len += 1
            return

        self.rear.next = temp
        self.rear = temp
        self.len += 1

    def deQueue(self):
        if self.is_empty():
            return

        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None

        self.len -=1
        return temp.data
    
    def returnRear(self):
        return self.rear

    def returnRear(self):
        return self.front
    
    def returnLen(self):
        return self.len
    
pilha = Queue()
pilha.enQueue(13)
pilha.enQueue('levy')
pilha.enQueue(18)
print(pilha.deQueue())
print(pilha.deQueue())
print(pilha.deQueue())
print(pilha.deQueue())
print(pilha.returnLen())
