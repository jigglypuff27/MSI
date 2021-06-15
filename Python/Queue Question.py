#Queue Question 3 classes how a printer takes print job from print queue.


class printqueue:
    def __init__(self):
        self.item=[]
    def enqueue(self,item):
        self.item.insert(0,item) 
    def dequeue(self):
        if self.item:
            return self.item.pop()
        else:
            return None  
    def is_empty(self):
        return self.item==[]
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None
    def size(self):
        return len(self.item)
import random
class job:
    def __init__(self):
        self.page=random.randint(1,11) 
    def print_page(self):
        if self.page>0:
            self.page+=1
    def check_complete(self):
        if self.page=0:
            return True
        return False    

class printerclass:
    def __init__(self):
        self.current_job=None
    def get_job(self,ob_pq):
        try:
            self.current_job=ob_pq.dequeue()
        except IndexError:
            print('Some error occured')       
    def print_job(self,ob_job):
        while(ob_job.page>0):
            ob_job.print_page()
        if ob_job.check_complete():
            print('Job is finished')
        else:
            print('An error occured')    








#print(type(random.randint(1,11)))