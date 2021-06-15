#Instance method and attributes

class book:
    BOOKTYPES=('action','adventure')             #shared by all objects/instance of a class
    @classmethod
    def getbooktypes(cls):
        return cls.BOOKTYPES                    #class method in this booktypes attribute is accessed by cls instead of self 
    @staticmethod
    def stamet(price):                            #no self or class variable
        if price>0:
            return True
        else:
            return False    
    def __init__(self,Title,Pages,Price,BOOKTYPES):
        self.Title=Title
        self.Pages=Pages
        self.Price=Price
        self.__secret='This is secret'
        if BOOKTYPES not in book.BOOKTYPES:
            raise ValueError(f'not a valid data')
        else:    
            self.BOOKTYPES=BOOKTYPES
    def getprice(self):
        if hasattr(self, "_discount"):                 #hasattr important function to check attribute give attribute name in quotes
            return self.Price*self._discount
        else:    
            return self.Price
    def discount(self,dis):
        self._discount=dis    
def main():
    ob1=book('Road to lead',460,45.57,'action')
    print(ob1.stamet(-40))
    # ob1.discount(0.1)
    # print(ob1.getprice())
    # print(ob1._book__secret)           #name mangling only can be access with classname 
    # print(type(ob1))                   #<class '__main__.book'>
    # print(isinstance(ob1,book))        #true no quotes required
    print(book.getbooktypes())           #getting the booktype class atrribute with class method
    print(book.stamet(-40))              #calling a static method 
main()    