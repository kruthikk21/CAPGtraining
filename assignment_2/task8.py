class animal:
    def speak(self):
        print("Animal speaks")
class dog(animal):
    def speak(self):
        print("Dog barks")
class cat(animal):
    def speak(self):
        print("mewoe")
obj=dog()
obj2=cat()
obj.speak()
obj2.speak()

