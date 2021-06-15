#Set

set1=set("hi my name is anthony gonzalvie's")
set2=set("mai duniya me awara hun's")
print(set1)  #output {'t', 'g', 's', 'n', ' ', 'y', 'm', 'i', 'h', 'a', 'z', 'l', 'v', "'", 'o', 'e'}


for i in set1:
    print(i,end='')
    #output tgsn ymihazlv'oe
def print_set(s):
    for i in s:
        print(i,end='')
set3=set1-set2   #members in a not in b    
print_set(set3)    

set3=set1 | set2
print_set(set3)

set3=set1 & set2
print(sorted(set3))