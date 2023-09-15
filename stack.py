from node import Node

class Stack():
    def __init__(self,data = None) -> None:
        self.head = None
        self.length = 0
        if data:
            for data in data:
                self.push(data)
    
    def push(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def pop(self):
        if self.head is None:
            raise IndexError('Lista vazia impossível executar esta operação')
        aux = self.head.data
        self.head = self.head.next
        return aux
    
    def isEmpty(self):
        return False if self.head else True
    
    def peek(self):
        return self.head.data if self.head else 'Lista vazia'
    
    def verifyDelimiter(self,expression):
        delimiters = Stack()
        for deli in expression:
            if deli in '([{':
                delimiters.push(deli)
            if deli in ')]}':
                if delimiters.isEmpty():
                    return False
                pop = delimiters.pop()
                if pop == '(' and deli != ')':
                    return False
                if pop == '[' and deli != ']':
                    return False
                if pop == '{' and deli != '}':
                    return False
        return delimiters.isEmpty()
        
    
pilha = Stack()
pilha.push(12)
pilha.push(13)
print(pilha.peek())
print(pilha.verifyDelimiter('[(axb)]'))