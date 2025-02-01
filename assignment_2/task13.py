class shape:
    def area(self):
        pass
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print("Area of square:",self.side*self.side)
class triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print("Area of triangle:",0.5*self.base*self.height)
obj1=triangle(10,20)
obj1.area()
obj2=square(10)
obj2.area()



        