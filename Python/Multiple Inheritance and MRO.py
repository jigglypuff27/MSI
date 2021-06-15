#Multiple Inheritance and MRO(method resolution order)

class A:
    def __init__(self,var1):
        self.name='Hi I am class A'
        self.var1=var1
class B:
    def __init__(self,var2):
        self.name='Hi I am class B'
        self.var2=var2

class C(B,A):
    def __init__(self,var3):
        super().__init__(var3)
        self.var3=var3
    def get(self):
        print(self.name)
        print(self.var3)        

ob1=C(4)
ob1.get()     
# O/P Hi I am class B
#4
print(C.__mro__)
# as per given in the class defination C(B,A) (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
