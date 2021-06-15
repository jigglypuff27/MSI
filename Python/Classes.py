class myclass():
    def method1(self):                          # It basically refer to object itself, in this method it refers to this particular instance of object that is being operated upon
        print('I am method1 inside myclass')
    def method2(self,var1):
        print('I am method2 inside myclass' , var1)

# c=myclass()          #instantiate an object of class
# c.method1()
# c.method2("hello")


class anotherClass(myclass):
    def method1(self):
        myclass.method1(self)               #important calling method1 of myclass
        print('I am method1 in anotherclass')
    def method2(self,var1):
        print('I am method2 in anotherclass')



c2=anotherClass()
c2.method1()              # calls the method1 of another class , inside method1 of another class =>method1 of myclas is called.
c2.method2("hello2")      # method2 of myclass is overridden my method2 of anotherclass