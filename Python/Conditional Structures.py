#Conditional Structures

def compare():
    x,y=2,3
    if(x<y):
        str="x is less than y"
    elif(x>y):
        str="x is greater than y"
    else:
        str="xis equal to y"
    print(str)
    str="x is less than y" if(x<y) else "x is greater or equal to y"  #this si cool
    print(str)

if __name__ == "__main__":
    compare()                