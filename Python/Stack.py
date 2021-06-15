'''Stack Implementation'''

class stack:
    def __init__(self):
        self.item=[]
    def push(self,item):
        self.item.append(item)        
    def pop(self):
        if self.item:
            return self.item.pop()
        else:
            return None
    def size(self):
        return len(self.item)
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None
    def is_empty(self):
        return self.item==[]                                 
def main():
    input_string=input()
    ob1=stack
    for i in input_string:
        if i in ['{','(','[']:
            ob1.push(i)
        else:
            if ob1.is_empty():
                return False
            else:
                    