class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
         
    def insertBeginning(self,data):
        node = Node(data)
        if self.length == 0:
            self.head = node
            self.length = 1
            return
        node.next = self.head
        self.head = node
        self.length += 1    

    def printList(self):
        node_aux = self.head
        while node_aux != None:
            print(node_aux.data)
            node_aux = node_aux.next

    def getLength(self):
        return self.length
    
    def insertEnd(self,data):
        node = Node(data)
        node_aux = self.head
        while node_aux.next != None:
            node_aux = node_aux.next
        node_aux.next = node
        self.length += 1
    def insertPosisition(self, data, pos):
        if pos > self.length:
            return 'posição invalida'
        node = Node(data)
        node_aux = self.head
        count = 0
        while count < pos - 1:
            count +=1
            node_aux = node_aux.next
        node.next = node_aux.next
        node_aux.next = node
        self.length += 1

lista_encadeada = LinkedList()
lista_encadeada.insertBeginning('levy')
lista_encadeada.insertBeginning('jorge')
lista_encadeada.insertBeginning('careca')
lista_encadeada.insertBeginning('jon')
lista_encadeada.insertEnd('barros')
lista_encadeada.insertEnd('barros')
lista_encadeada.insertPosisition(3,5)
lista_encadeada.printList()
print(lista_encadeada.getLength())