#Abstract method


#Abstarct method can't be accessed directly the class object.
#method defined inside the abstract class needs to be override by class which inherit
#we use abc module
from abc import ABC,abstractmethod

class baseclass(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod    
    def calArea(self):
        pass    

class inherit(baseclass):
    def __init__(self,para):
        self.para=para
    def calArea(self):     #if we dont overiride this class it will give TypeError: Can't instantiate abstract class inherit with abstract method calArea
        return 2*self.para     
def main():
    ob1=inherit(25)
    print(ob1.calArea())
    #ob2=baseclass()        #cannot access class by objectTypeError: Can't instantiate abstract class baseclass with abstract method calArea

main()                