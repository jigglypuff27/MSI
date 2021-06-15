#Doubly Linked List

#Singly linked list

class DLLNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
    def set_data(self,n_data):
        self.data=n_data  
    def get_data(self):
        return self.data
    def set_next(self,n1):
        self.next=n1
    def get_next(self):
        return self.next
    def __repr__(self):
        return f'Data in node {self.data}'  
    def get_previous(self):
        return self.previous
    def set_previous(self,p1):
        self.previous=p1




node1=DLLNode('aPPLE')
node2=DLLNode('Banana')
node3=DLLNode('ME')
print(node1.get_data())
node1.set_data('Apple')
node1.set_next(node2)
node2.set_next(node3)

print(node2.get_next())

node2.set_previous(node1)
node3.set_previous(node2)
print(node2.get_previous())


