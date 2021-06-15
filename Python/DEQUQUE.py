#DEQUQUE
#both FIFO AND/OR LIFO 

class dequeue:
    def __init__(self):
        self.item=[]
    def add_front(self,val1):
        self.item.insert(0,val1)
    def add_rear(self,val2):
        self.item.append(val2)
    def remove_front(self):
        if self.item:
            return self.item.pop(0)
        else:
            return None 
    def remove_rear(self):
        if self.item:
            return self.item.pop()
        else:
            return None
    def peek_front(self):
        if self.item:
            return self.item[0] 
        else:
            return None
    def peek_rear(self):
        if self.item:
            return self.item[-1]
        else:
            return None
    def is_empty(self):
        return self.item==[]


input1=input()
ob1=dequeue()
if (len(input1)==1):
    print('pallindrome')
else: 
    temp=0   
    for i in range(0,len(input1)):
        ob1.add_front(input1[i])
        ob1.add_rear(input1[len(input1)-1-i])
        print(ob1.peek_front(),ob1.peek_rear())
        if ob1.remove_front()==ob1.remove_rear():
            
            continue
        else:
            #print('not a pallindrome')
            temp=1
            break
    if(temp==1):
        print('Not a pallindrome')
    else:        
        print('pallindrome')     

