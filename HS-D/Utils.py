import random
class Utils:
    def __init__(randomseed):
        self.randomseed=5
        random.seed(self.randomseed)

    def weighted_random(_list,weight=None):
        if(weight==None):
            weight=[0]*len(_list)
        if(len(weight)!=len(_list)):
            print("Error: not the same Length")
            return
        t = random.randint(0, sum(weight) - 1)
        for i,val in enumerate(weight):
            t-=val
            if t<0:
                return _list[i]

    def chooseRandomFromList(_list,num):
        chosen=random.sample(_list,num)
        return chosen
    
    def shuffle(_list):
        l=_list.copy()
        return random.shuffle(l)

    def randint(min,max):
        return random.randint(min,max);

class _Int:
    def __init__(self, n=0):
        self.value = n

    def __eq__(self, value):
        if(isinstance(other,_Int)):
            return self.value==other.value
        if(isinstance(other,int)):
            return self.value==other
        return false

    def __add__(self, other):
        if(isinstance(other,_Int)):
            self.data=self.data + other.data
        if(isinstance(other,int)):
            self.data=self.data + other

    def __mul__(self,other):
        if(isinstance(other,_Int)):
            self.data=self.data * other.data
        if(isinstance(other,int)):
            self.data=self.data * other
    
    def __sub__(self,other):
        if(isinstance(other,_Int)):
            self.data=self.data - other.data
        if(isinstance(other,int)):
            self.data=self.data - other

    def __truediv__(self,other): #override to floordiv
        if(isinstance(other,_Int)):
            self.data=self.data // other.data
        if(isinstance(other,int)):
            self.data=self.data // other

    def __floordiv__(self,other): #override to truediv
        if(isinstance(other,_Int)):
            self.data=self.data / other.data
        if(isinstance(other,int)):
            self.data=self.data / other

    def __mod__(self,other): 
        if(isinstance(other,_Int)):
            self.data=self.data % other.data
        if(isinstance(other,int)):
            self.data=self.data % other

    def __pow__(self,other): 
        if(isinstance(other,_Int)):
            self.data=self.data ** other.data
        if(isinstance(other,int)):
            self.data=self.data ** other

    def get(self):
        return self.value

    def set(self,value):
        self.value=value

class Limited_Int(_Int):
    def __init__(self, max, min=None, value=None):
        self.max=max
        self.min=min
        if(value!=None):
            self.value=value
        else:
            self.value=max

    def __eq__(self, value):
        if(isinstance(other,_Int)):
            return self.value==other.value
        if(isinstance(other,int)):
            return self.value==other
        return false

    def __add__(self, other):
        super().__add__(other)
        if(self.value>max):
            self.value=max
        if(min!=None):
            if(self.value<min):
                self.value=min

    def __mul__(self,other):
        super().__mul__(other)
        if(self.value>max):
            self.value=max
        if(min!=None):
            if(self.value<min):
                self.value=min
    
    def __sub__(self,other):
        super().__sub__(other)
        if(self.value>max):
            self.value=max
        if(min!=None):
            if(self.value<min):
                self.value=min

    def __truediv__(self,other): #override to floordiv
        super().__truediv__(other)
        if(self.value>max):
            self.value=max
        if(min!=None):
            if(self.value<min):
                self.value=min

    def __floordiv__(self,other): #override to truediv
        super().__floordiv__(other)
        if(self.value>max):
            self.value=max
        if(min!=None):
            if(self.value<min):
                self.value=min

    def __mod__(self,other): 
        super().__mod__(other)
        if(self.value>max):
            self.value=max
        if(min!=None):
            if(self.value<min):
                self.value=min

    def __pow__(self,other): 
        super().__pow__(other)
        if(self.value>max):
            self.value=max
        if(min!=None):
            if(self.value<min):
                self.value=min

    def get(self):
        return self.value

    def set(self,value):
        self.value=value



class DefaultSettings():
    def __init__(self):
        self.MAX_HREO_NUM=1
        self.MAX_HAND_NUM=10
        self.MAX_DECK_NUM=60
        self.MAX_CRYSTAL_NUM=10