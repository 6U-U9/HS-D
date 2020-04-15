import Utils
class Crystal(Utils.Limited_Int):
    def __init__(self):
        self.state="empty"
        self.value=1
        

    def use(self):
        if(self.value>0):
            self.state="empty"
            return self.value

    def refresh(self):
        if(self.state!="overloaded"):
            self.


