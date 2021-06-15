#More into Self

class myclass():
    schoolname="St. Xaviers"
    Batch="A2"
    #Basically self is an object which refers to this particular instance
    def func1(self):
        return self.schoolname


def main():
    if False:
        print(1)
    elif True:
        print(2)
    elif True:
        print(3)    
    else :
        print(4)        

    c=myclass()
    #print(c.func1())
main()
