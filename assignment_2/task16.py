from abc import ABC, abstractmethod
class Ishape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(Ishape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("Area of rectangle:",self.length*self.breadth)
class circle(Ishape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("area of circle is:",3.14*self.radius*self.radius)
obj1=rectangle(10,20)
obj1.area()
obj2=circle(10)
obj2.area()
