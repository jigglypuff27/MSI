#Inheritance Basic

class cricket:
    def __init__(self,**kwargs):
        if 'type' in kwargs: self._type=kwargs['type']
        if 'activity' in kwargs: self._activity=kwargs['activity']
        if 'rating' in kwargs: self._rating=kwargs['rating']

    def getsettype(self,t=None):
        if t: self._type=t
        try: return self._type
        except AttributeError: return None
    def getsetactivity(self,t=None):
        if t: self._activity=t
        try: return self._activity
        except AttributeError: return None
    def getsetrating(self,t=None):
        if t: self._rating=t
        try: return self._rating
        except AttributeError: return None             

    def __str__(self):
        return f'{self.getsettype()}, {self.getsetactivity()}, {self.getsetrating()}' 

class ratingclass(cricket):
    def __init__(self,**kwargs):
        self._rating=0
        if 'rating' in kwargs: del kwargs['rating']
        super().__init__(**kwargs)            #super() used to call constructor of base class

obj1=cricket(type='himanshu',activity='all rounder',rating=10)
print(obj1)

obj2=ratingclass()
print(obj2)

