from abc import ABC , abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def area(self,l,b):
        print(l*b)
class circle(shape):
    def area(self,r):
        print(3.14*r*r)

obj1 = rectangle()
obj1.area(5,6)
obj2 = circle()
obj2.area(4)