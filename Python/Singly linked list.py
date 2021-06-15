#Singly linked list

class SLLNode:
    def __init__(self,data):
        self.data=data
        self.next=None
    def set_data(self,n_data):
        self.data=n_data  
    def get_data(self):
        return self.data
    def set_next(self,n1):
        self.next=n1
    def get_next(self):
        return self.next
    def __repr__(self):  #It allows you to specify what descriptive text should be shown when you print an instance of a class.
        return f'Data in node {self.data}'        


node1=SLLNode('aPPLE')
node2=SLLNode('Banana')
node3=SLLNode('ME')
print(node1.get_data())
node1.set_data('Apple')
node1.set_next(node2)
node2.set_next(node3)

print(node2.get_next())


