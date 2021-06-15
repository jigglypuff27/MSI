#List comprehension



def print_list(l):
    for i in l:
        print(i)


list1= range(1,10)
#print_list(list1)   

list2=[x*2 for x in list1]
#print_list(list2)
list3=[x*2 for x in list1 if x%2==0]
#print_list(list3)

tuple1=[(x,x/2) for x in list1]
print_list(tuple1)

dict1={x:x/3 for x in list3}
for i,v in dict1.items():
    print(f'{i}:{v}')