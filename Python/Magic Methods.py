#Magic Methods

class myclass:
    def __init__(self,title,author,page):
        self.title=title
        self.author=author
        self.page=page
    def __str__(self):                  #overriding by default str function
        return f'book name{self.title}, book author {self.author}'
    def __repr__(self):                   #overriding by default repr function
        return f'name is himanshu {self.page}'        
ob1=myclass('the book one','himanshu',277)
print(ob1) 
print(str(ob1))
print(repr(ob1))


# __eq__ override this method for == operator
# __lt__ override this method for < operator
# __ge__ override this method for >= operator
#built in sort method uses __lt__ operator so we can sort too eg: book=[b1,b2,b3,b4] book.sort()
