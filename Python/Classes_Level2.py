#Classes
class myclass:
    food1='maggie'
    food2='noodles'
    def eat(self):
        return self.food1
    def noteat(self):
        return self.food2    

def main():
    ob=myclass()
    print(ob.eat())
    print(ob.noteat())
main()