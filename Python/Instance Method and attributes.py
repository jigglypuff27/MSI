#Instance method and attributes

class book:
    def __init__(self,Title,Pages,Price):
        self.Title=Title
        self.Pages=Pages
        self.Price=Price
        self.__secret='This is secret'
    def getprice(self):
        if hasattr(self, "_discount"):                 #hasattr important function to check attribute give attribute name in quotes
            return self.Price*self._discount
        else:    
            return self.Price
    def discount(self,dis):
        self._discount=dis    
def main():
    ob1=book('Road to lead',460,45.57)
    ob1.discount(0.1)
    print(ob1.getprice())
    print(ob1._book__secret)           #name mangling only can be access with classname 
    print(type(ob1))                   #<class '__main__.book'>
    print(isinstance(ob1,book))        #true no quotes required
main()    