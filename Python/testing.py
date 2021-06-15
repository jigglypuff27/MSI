# #testing

# def main():
#     ob1=open('textfile.txt','r')
#     ob2=open('textfile27.txt','w+')
#     # for i in ob1:
#     #     print(i.rstrip())
#     for i in ob1.readlines():
#         ob2.write(i)
    
#     ob1.close()
#     ob2.close()
        
# #abcdemain()        

# def pallindrome():
#     str1=input('enter a string')
#     str2=str1[::-1]
#     if str1==str2:
#         print('pallindrome')
#     else:
#         print('not a pallindorme')
# pallindrome()        


'''
def func1():
    l=[1,2,3,4,5,4,1,2,1]
    d=dict()
    for i in l:
        if i not in d:
            d[i] = 0
        else:
            d[i] +=1
    #for i in l:
    #    d[i]=d[i]+1
    for k,v in d.items():
        print(f'{k},{v}')
    max1=max(d.values())
    


#func1()        



str1='xyz'
str2='abcxyav'
for i in str1:
    if i in str2:
        print(i)

l=[1,1]
#print(len(l))
lenght=len(l)-1
for i in range(0,lenght):
    if(i>=len(l)-1):
            break
    if l.count(l[i])>1:
        #print(f'i={i},count={l.count(l[i])}')
        del l[(i+1):i+(l.count(l[i]))]
        #print("deleted")
        #print(l)
        #length=len(l)-l.count(l[i])
        
        #print('length',length)
#print(l)        
'''
nums = [0,1,2,2,3,0,4,2]
val = 2
nums= [i for i in nums if i !=val]
nums = [i for i in nums if i != val]
print(nums)