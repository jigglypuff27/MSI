#Inheritance in deep

class maggie:
    def __init__(self,price,type1):
        self.price=price
        self.type=type1

class aatamaggie(maggie):
    def __init__(self,price,type1,nutri,shape):
        super().__init__(price,type1)             #calling constructor of base class no self is provided in arguments
        self.nutri=nutri
        self.shape=shape

def main():
    ob1=aatamaggie(127,'aata',45,'round')
    print(ob1.shape,ob1.price)
main()