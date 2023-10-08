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

    @staticmethod
    def infixToPosfix(expression):
        stack = Stack()
        for char in expression:
            if char not in '+-/*':
                stack.push(char)
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                if char == '+':
                    stack.push(int(pop1) + int(pop2))
                if char == '-':
                    stack.push(int(pop1) - int(pop2))
                if char == '*':
                    stack.push(int(pop1) * int(pop2))
                if char == '/':
                    stack.push(int(pop1) // int(pop2))
        return stack.pop()
    
    @staticmethod
    def makeCalc(num1,num2,op):
        if op == '+':
            return int(num1) + int(num2)
        if op == '-':
            return int(num1) - int(num2)
        if op == '*':
            return int(num1) * int(num2)
        if op == '/':
            return int(num1) // int(num2)
        
    @staticmethod
    def calculePos(expression):
        pilha = Stack()
        for char in expression:
            if char in '+-/*':
                num11 = pilha.pop()
                num22 = pilha.pop()
                result =  pilha.makeCalc(num22,num11,char)
                pilha.push(result)
            else:
                pilha.push(char)
        return pilha.pop()
                
        
    
pilha = Stack()
pilha.push(12)
pilha.push(13)
print(pilha.peek())
print(pilha.verifyDelimiter('[(axb)]'))
print(pilha.calculePos('123*+5-'))
