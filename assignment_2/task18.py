from abc import ABC, abstractmethod
class Icalculator:
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    @abstractmethod
    def mul(self):
        pass
    @abstractmethod
    def div(self):
        pass
class basic_calculator(Icalculator):
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            print("cant divide by zero")
        else:
            return a/b
obj=basic_calculator()
print("Addition:",obj.add(9,6))
print("substraction:",obj.sub(56,45))
print("multiplication:",obj.mul(85,5))
print("division",obj.div(78,2))
obj.div(5,0)
        
