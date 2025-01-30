from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class dog(Animal):
    def make_sound(self):
        print("Bark")
class cat(Animal):
    def make_sound(self):
        print("meow")

dog=dog()
cat=cat()
dog.make_sound()
cat.make_sound()

