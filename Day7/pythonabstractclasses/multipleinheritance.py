from abc import ABC, abstractmethod
class person(ABC):
    @abstractmethod
    def get_name(self):
        pass
class employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass
class manager(person,employee):
    def get_name(self):
        print("Name is Manager")
    def get_salary(self):
        print("Salary is 50000")
obj1=manager()
obj1.get_name()
obj1.get_salary()
