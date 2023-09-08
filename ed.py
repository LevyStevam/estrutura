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
            print(node_aux.data, end=' | ')
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
        
    def insertPosition(self, data, pos):
        node = Node(data)
        node_aux = self.head
        count = 0
        while count < pos - 1 and node_aux.next != None:
            count +=1
            node_aux = node_aux.next
        node.next = node_aux.next
        node_aux.next = node
        self.length += 1
        
    def fullForce(self,n):
        position = 0
        node_aux = self.head
        while node_aux.next != None:
            position += 1
            node_aux = node_aux.next
        target = position - (n + 1)
        count = 0
        node_aux = self.head
        while count <= target:
            node_aux = node_aux.next
            count += 1
        
        return node_aux.data
        
    
    def fastslow(self, n):
        fast =  slow = self.head
        
        count = 0
        
        while count < n:
            count +=1
            fast = fast.next
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        return slow.data
        
    
    def printarinverso(self, node = None):
        if node == None:
            node = self.head
            
        if node.next != None:
            self.printarinverso(node.next)
        
        print(node.data)
        
    def insertInOrder(self, data):
        
        if self.head == None:
            return
        
        if data < self.head.data:
            return self.insertBeginning(data)
        
        current = self.head
        position = 0
        while current.next != None:
            if data > current.data and data <= current.next.data:
                return self.insertPosition(data, position + 1)
                
            position += 1
            current = current.next

    def removeAllK(self,data):
        previous = self.head
        current = self.head.next
        if self.head.data == data:
            while self.head.data == data:
                self.head = self.head.next
                previous = previous.next
                current = current.next
        while current.next is not None:
            if current.data == data:
                previous.next = current.next
                current = current.next
                self.length -= 1
            else:
                current = current.next
                previous = previous.next

    
    def removeAtPosition(self, pos):
        if pos == 0 :
            self.head = self.head.next
        count = 0
        previous = self.head
        current = self.head.next
        while current.next is not None:
            if pos == count:
                previous.next = current.next
                return
            current = current.next
            previous = previous.next
            count += 1
        previous.next = None
        return
    
    #questão da prova inverte pares.
    def switchPar(self):
        current = self.head
        while current.next is not None:
            aux = current.data
            current.data = current.next.data
            current.next.data = aux
            current = current.next.next
    
    #remove iguais numa lista ordenada
    def removeAllEqual(self):
        current = self.head
        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        
        

lista_encadeada = LinkedList()
lista_encadeada.insertBeginning(12)
lista_encadeada.insertBeginning(9)
lista_encadeada.insertBeginning(8)
lista_encadeada.insertBeginning(8)
lista_encadeada.insertEnd(15)
# lista_encadeada.insertBeginning(1)
#lista_encadeada.insertInOrder(10)
# lista_encadeada.insertPosition(5,4)
lista_encadeada.insertInOrder(13)
# lista_encadeada.removeAllK(8)
lista_encadeada.insertEnd(18)
lista_encadeada.printList()
print()
lista_encadeada.switchPar()
lista_encadeada.printList()
lista_encadeada.removeAllEqual()
print()
lista_encadeada.printList()
#print('\n')
#print(lista_encadeada.fullForce(5))
#print(lista_encadeada.fastslow(5))
#print('\n')
#print('\n')
#lista_encadeada.printarinverso()
