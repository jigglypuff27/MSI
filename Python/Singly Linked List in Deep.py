#Singly Linked List in Deep

class SLLNode:
    def __init__(self,data):
        self.data=data
        self.next=None
    def set_data(self,data):
        self.data=data
    def get_data(self):
        return self.data
    def set_next(self,n1):
        self.next=n1
    def get_next(self):
        return self.next

class SLL:
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head is None
    def add_front(self,data):         #  nothing self.head should point to new node which has been created 
        node=SLLNode(data)            # if something already present eg: 1->None self.head=nodeof1 result needed:-[2->1->none]:- operations 1)newnodeof2.next->self.head 2)self.head=newnodeof2 
        node.set_next(self.head)
        self.head=node
    def size(self):
        count=0
        if self.head is None:
            return 'Linked list is empty'
        current=self.head
        while(current is not None):
            count+=1
            current=current.get_next()
        return count

    def search(self,data):
        if self.head is None:
            return 'Linked list is empty'
        current=self.head
        while current is not None:
            if current.get_data()==data:
                return True
            current=current.get_next()    
        return False
    def remove(self,data):
        if self.head is None:
            return 'Linked List is empty nothing to remove'
        else:
            if self.search(data):
                current=self.head
                previous=None
                while current is not None:
                    if current.get_data()==data:   #1->None   2->1->3->None  3->2->1->None 3 cases
                        if previous is None:
                            previous=self.head.get_next()
                        else:    
                            previous.set_next(current.get_next())
                        return 'A node with data is found'
                    previous=current
                    current=current.get_next()        
            else:
                return 'Not found'                                    
    def __repr__(self):
        return f'Object instance data {self.head}'

n1=SLL()
n1.add_front(1)
n1.add_front(2)
n1.add_front(3)
n1.add_front(4)
n1.add_front(5)

print(n1.size())
print(n1.search(1))
print(n1.search(3))
print(n1.search(5))
print(n1.search(7))

print(n1.remove(7))
print(n1.remove(5))
print(n1.head.get_data())
#print()
#print(n1.remove)

#debug this program