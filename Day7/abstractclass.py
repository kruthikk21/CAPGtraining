from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def show(self):  # This is a concrete method
        print("This is an abstract class concrete method.")

class Dog(Animal):
    def speak(self):
        print("Dog sound's like Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat sound's like Meow!")

dog = Dog()
cat = Cat()
dog.show()
cat.show()
dog.speak()
cat.speak()

# animal = Animal() # This will raise an error, because we cannot create an object of an abstract class