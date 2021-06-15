#Python Essentials




def isprime(num1):
    if num1 <= 1:
        return False
    for i in range(2,num1):
        if num1%i == 0 :
            return False
    return True        


def listofprime(var1):
    for i in range(var1):
        res=isprime(i)
        if res:
            print(i)     
def main():
    x=42
    print("my name is {}".format(x))
    print(f"my name is {x}")
    print("my name is "+str(x))
    listofprime(100)
main()    