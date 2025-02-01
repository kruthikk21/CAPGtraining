class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class employee(person):
    def __init__(self,name,age,empid,salary):
        super().__init__(name,age)
        self.empid=empid
        self.salary=salary
    def display(self):
        super().display()
        print("Employee ID:",self.empid)
        print("Salary:",self.salary)
class manager(employee):
    def __init__(self,name,age,empid,salary,department):
        super().__init__(name,age,empid,salary)
        self.department=department
    def display(self):
        super().display()
        print("Department:",self.department)
    def approve_leave(self):
        print("Leave has been approved for",self.name)

obj2=employee("kruthik",21,"21h51a6206",50000)
obj3=manager("kruthik",21,"21h51a6206",50000,"CSE")
obj3.display()
obj3.approve_leave()


