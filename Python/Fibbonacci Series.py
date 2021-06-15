#Fibbonacci Series
def fib(num1):
    startpoint=0
    nextpoint=1
    if(num1<0):
        return None
    l=[0]
    #print('hi')
    for i in range(num1-1):
        if num1==1:
            l.append(num1)
            return l
        else :
            nextvalue=startpoint+nextpoint
            startpoint=nextpoint
            nextpoint=nextvalue
            l.append(nextvalue)    
    return l    

def valueat(num2):
    l=fib(num2)
    return l[num2-1]

def main():
    print(fib(10))
    print(valueat(10))

main()