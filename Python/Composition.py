#Composition :-creating relationship between classes and its objects.

class Book:
    def __init__(self, title,price,author=None):
        self.title=title
        self.price=price
        self.author=author
        self.chapter=[]

    def addchapter(self,chapter):
        self.chapter.append(chapter) 

    #def __str__(self):
               
class Author:
    def __init__(self,name,rank):
        self.name=name
        self.rank=rank

class chapter:
    def __init__(self,chaptername,noofpages):
        self.chaptername=chaptername
        self.noofpages=noofpages                


auth=Author('Himanshu Sahu',72)
book=Book('this book',27,auth)
ch1=chapter('chapter1st',9)
book.addchapter(ch1)

print(book.title)


#play with it for composition