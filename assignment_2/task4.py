class student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Rollno:",self.rollno)
obj=student("kruthik",21,"21h51a6206")
obj.display()

        