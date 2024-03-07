class shapes:
    def __init__(self,len,bred):
        self.length=len
        self.breadth=bred
    def areas(self):
        self.area=self.length*self.breadth
        print(self.area)

class rectangle(shapes):
    def __init__(self,len,bred):
        shapes.__init__(self,len,bred)

class square(shapes):
    def __init__(self,len,bred):
        rectangle.__init__(self,len,bred)
    
objct1=rectangle(5,3)
objct2=square(3,3)
objct1.areas()
objct2.areas()