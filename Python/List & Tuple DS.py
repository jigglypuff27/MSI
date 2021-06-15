#List & Tuple DS 


def func1():
    x= ['mon','tue','wed','thu','fri','sat']
    #print(x)       #print the list
    #to append something
    x.append("sun")
    #to insert at given index
    x.insert(0,"mon")
    #to delete via value (it deletes first mon)
    x.remove("mon")
    x.pop()       #removes items from end of the list
    removed_value=x.pop()    #pop return a remove value as well 
    print(removed_value)
    #to delete via index
    x.pop(1)          #removes an item at particular index
    del x[0]          #to delete an item at index 0
    del x[1:3]         #remove slice you know it
    #printing in patterns
    print(x[1])                    #o/p tue
    print(x[1:3])                  #list ['tue', 'wed']
    print(x[2:5:1])                #['wed', 'thu', 'fri']
    print(x[2:5:8])                 #['wed']
    print(x[2:5:-8])                #[]
    print(x[-2])                        #it takes backword index -2 = sat -1=sun like that
    #print(x[-8])                    #index out of range
    #print(x[9])                     #index out of range
    print(x[0:9])                   #['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    print(x[-1:9])                 #['sun']

    #searching via value
    print(x.index("sat"))           #o/p 5 
    print(x.index('hi'))           #ValueError: 'hi' is not in list


    #print_list(x)

    #to join a list 
    print(','.join(x))   #mon,tue,wed,thu,so on
    #to know length
    print(len(x))
def print_list(l):
    for i in l:
        print(i)         #print item one by one
func1()        
