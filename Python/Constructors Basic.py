# #Constructors Basic

# class cricket:
#     def __init__(self,name,activity,rating):         #class concstructor first argument is self used to initialize the objects and has name __init__
#         self._name=name                              #_before the variable so that it can't be accessed from outside directly.
#         self._activity=activity
#         self._rating=rating
#     def get_name(self):                              #getter/accessor function to access the variable
#         return self._name
#     def get_activity(self):
#         return self._activity
#     def get_rating(self):
#         return self._rating
# def print_class_objects(o):
#     #print(type(o))
#     if isinstance(o,cricket):                         #check the object is of cricket type or not
#         print(o.get_name(),o.get_activity(),o.get_rating())

# def main():
#     ob1=cricket('kohli','batsman',10)
#     ob2=cricket('bhuvi','bowler',10) 
#     print_class_objects(ob1)
#     print_class_objects(ob2)
#     print_class_objects(cricket('dhoni','captain',10))    #directly its possible function call work as an assignments in python

# main()    
                       

#to remove the order we will use **kwargs  same code little change                



#Constructors Basic

class cricket:
    def __init__(self,**kwargs):         #class concstructor first argument is self used to initialize the objects and has name __init__
        self._name=kwargs['name'] if 'name' in kwargs else 'himanshu'                             #_before the variable so that it can't be accessed from outside directly.
        self._activity=kwargs['activity'] if 'activity' in kwargs else 'all rounder'     #default value is assigned
        self._rating=kwargs['rating'] if 'rating' in kwargs else 10
    def get_name(self):                              #getter/accessor function to access the variable
        return self._name
    def get_activity(self):
        return self._activity
    def get_rating(self):
        return self._rating
def print_class_objects(o):
    #print(type(o))
    if isinstance(o,cricket):                         #check the object is of cricket type or not
        print(o.get_name(),o.get_activity(),o.get_rating())

def main():
    ob1=cricket(name='kohli',activity='batsman',rating=10)
    ob2=cricket() 
    print_class_objects(ob1)
    print_class_objects(ob2)
    #print_class_objects(cricket('dhoni','captain',10))    #directly its possible function call work as an assignments in python

main()    
               