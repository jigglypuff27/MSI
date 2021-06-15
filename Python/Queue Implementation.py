#Queue Implementation

class Queue:
    def __init__(self):
        self.item=[]
    def enqueue(self,item):
        self.item.insert(0,item)        #O(N) and rest all methods are O(1) constant time
    def dequeue(self):
        if self.item:
            return self.item.pop() 
        else:
            return None
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None
    def size(self):
        return len(self.item)
    def is_empty(self):
        return self.item==[] 

ob1=Queue()
ob1.enqueue('Apple')
ob1.enqueue('Banana')
ob1.enqueue('Orange')
print(ob1.dequeue()) 
print(ob1.is_empty())
print(ob1.peek())
print(ob1.size())

print(ob1.item)