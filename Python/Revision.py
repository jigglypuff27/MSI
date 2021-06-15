# # #Revision

# # x=0
# # while(x<10):
# #     print(x,end='')
# #     x+=1
# # for i in range(5,10):
# #     if i%2==0:
# #         break
# #     print(i,end='')

# # l1=['hi','hello','bye','goodbye']
# # for i in l1:
# #     print(i)    
# # for i,v in enumerate(l1):
# #     print(f'index={i},value={v}')    

# # a=['1','h','hi','hi123','}',' ']
# # for i in a:
# #     if i.isdecimal():
# #         print('its numerical')
# #     elif i.isalnum():
# #         print('its alphanumeric')
# #     else:
# #         print('something other')    


# # def fun1():
# #     print('hi')
# # fun1()
# # print(fun1()) 
# # print(fun1)   

# # def fun2(arg1,arg2):
# #     print(f'{arg1},{arg2}')
# # fun2(2,4) 

# # def fun3(*args):
# #     for i in args:
# #         print(i,end='')
# #     return True    
# # fun3(1,2,3,4,5,6)      
# # print(fun3(1,2))  

# # class myclass:
# #     def func1(self):        #slef refers to the object itself, this self in this function refers to the particular instance of that object which its been acted upon.
# #         print('Hi i am func1')
# #     def func2(self,var1):
# #         print(f'Hi i am func2,{var1}')    


# # obj1=myclass()
# # obj1.func1()
# # print(obj1.func2(5))

# # class anotherclass:
# #     def func3(self):
# #         print('calling the func1')
# #         myclass.func1(self)         
# #     def func4(self,var2):
# #         print('Hi i am func4') 
# # obj2=anotherclass()
# # obj2.func3()
# # obj2.func4(5)           



# # import math
# # print(f'{math.pi:0.2f}')

# # print(f'{math.ceil(7.9)}')

# # from datetime import datetime
# # from datetime import date
# # from datetime import time
# # present_time=date.today()
# # print(present_time.year,present_time.month,present_time.day)
# # present_timestamp=datetime.now()
# # print('extracting components')
# # print(present_timestamp.year,present_timestamp.month,present_timestamp.day,datetime.time(present_timestamp))


# # from datetime import timedelta
# # time1=timedelta(days=375,hours=3,minutes=5,seconds=45)
# # print(str(datetime.now()-time1))
# # date1=date(month=4,day=1,year=2021)
# # print(str(date.today()-date1))


# # f=open('newfile.txt','w+')
# # for i in range(1,10):
# #     f.write(f'Hi i am line{i}')
# # f.close()

# # f=open('newfile.txt','r')
# # for i in f.readlines():
# #     print(i)
# # f.close()    

# # f=open('newfile.txt','a')
# # if f.mode=='a':
# #     print('hi')
# # f.close()    


# # import os 
# # from os import path

# # print(path.exists('newfile.txt'))
# # print(path.isdir('newfile.txt'),path.isfile('newfile.txt'))
# # print(path.realpath('newfile.txt'))
# # print(path.split(path.realpath('newfile.txt')))

# # #os.rename('newfile1.txt','newfile.txt')

# # #use shutil to copy the file

# # #extarcting data from internet

# # import urllib.request
# # extract=urllib.request.urlopen('https://www.google.com')
# # print(extract.read())




# # def isprime(num1):
# #     if num1<=1:
# #         return False
# #     else:
# #         for i in range(2,num1):
# #             if num1%i==0:
# #                 return False
# #         return True            

# # for i in range(0,100):
# #     if isprime(i):
# #         print(i)  


# # def gen(start,stop):
# #     while(start<=stop):
# #         yield start
# #         start+=1
# # for i in gen(0,10):
# #     print(print(i))        

# # f=open('testfile_1.txt','w+')
# # for i in range(1,350000):
# #     f.write(f'This is line number {i} and this is created for test purpose kindly ignore the data please and hi bye goodbye heello')
# # f.close()    



# l1=['hi','hello','bye','goodbye']
# for i,v in enumerate(l1):
#     print(i,v)

# #to delete we use ,remove and del :- pop can delete the element taking index as arguments and returns the deleted value, del also delete the element at index and returns nothing and remove delete the element based on the value
# #     
# l1.pop()    
# l1.pop(0)
# del l1[0]      #we can use indexing or range things here
# l1.remove('bye')
# print(l1)

# #to insert we use insert and append method
# l1.insert(0,'hi')
# print(l1)
# l1.append('hello')   #append at the last it increase the lenght of the list by 1 its just append the object at the last
# l3=['good','goodbye']
# l1.extend(l3)       #in extend it iterates through all the elemetns presetn in the arguments (list) and append all those elements in the last so increase the lenthg of the list by number of elements present in the arguments

# print(l1)

# #indexing in list
# print(l1[::-1]) #reverses a list
# print(l1[1:3:1]) #output []
# print(l1[-1:-3:-1]) #ouput [goodbye,good]

# #to know the lenght len is used
# #to search index is used
# print(l1.index('hi'))

# print(':'.join(l1)) #it gives the string as output

# tuple1=('hi','hello','bye')
# #del tuple1[0]    #it will give error
# print(tuple1)
# #tuple1[0]='hello'   #cant assign
# print(tuple1)


# dict1={'morning':'breakfast','noon':'lunch','night':'dinner'}
# for k,v in enumerate(dict1):
#     print(f'{k},{v}')

# # items() to get key and value keys()  to get keys values() to get values
# for k in dict1.keys():
#     print(k)
# for v in dict1.values():
#     print(v)     
# str1='hello my name is himanshu27'
# set1=set(str1)
# print(set1)   #order doesn't matter has unique elements in it




# class myclass:
#     def __init__(self,name,specialist,rating):
#         self._name=name
#         self._specialist=specialist
#         self._rating=rating
#     def getname(self):
#         return self._name
#     def getspecialist(self):
#         return self._specialist
#     def getrating(self):
#         return self._rating
#     def print1(self,o):
#         if isinstance(o,myclass):
#             print(f'{self._specialist,self._name,self._rating}')
# ob1=myclass('virat','batsman',10)
# ob1.getspecialist()
# ob1.print1(ob1)                        

# #str(123+'abc')

# st1='hi my name is himanshu'
# print(str1.upper())
# print(str1.lower())
# print(str1.title())  #all first letter is capital
# print(str1.capitalize())  #only first letter
# print(str1.swapcase())



# print(st1.split()) #it split with spaces
# print(st1.split('h'))  #character gayab
# st2='xyz wvx'
# print(st2.join(st1))

# def fib():
#     start=0
#     second=1
#     print(start)
#     print(second)
#     next=0
#     for i in range(0,100):
#         next=start+second
#         start=second
#         second=next
#         print(next)
# fib()   


# def fibatindex(num1):
#     if num1==0 or num1==1:
#         return num1
#     start=0
#     next=1
#     newval=0
#     for i in range(1,num1):
#         #print('hi')
#         newval=start+next
#         start=next
#         next=newval
#     return newval
# for i in range(0,15):
#     print(fibatindex(i),end=' ')

import sqlite3

db=sqlite3.connect('data.db')
cur=db.cursor()
cur.execute('DROP TABLE IF EXISTS TEST')
cur.execute('CREATE TABLE TEST (NAME VARCHAR,CLASS VARCHAR,ROLLNUMBER NUMBER PRIMARY KEY)')
cur.execute("INSERT INTO TEST VALUES('HIMANSHU','12TH',1)")
for row in cur.execute("Select * from test"):
    print(row)
db.commit()
db.close()    

print(2.0==2)