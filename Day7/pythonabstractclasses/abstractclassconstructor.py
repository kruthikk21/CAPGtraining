from abc import ABC , abstractmethod

class vehicle(ABC):
    def max_speed(self):
        pass
    def __init__(self,brand):
        self.brand=brand
class car(vehicle):
    def __init__(self, brand):
        super().__init__(brand)
    def max_speed(self):
        print("max speed is 200kmph")
class bike(vehicle):
    def __init__(self, brand):
        super().__init__(brand)
    def max_speed(self):
        print("Max speed is 150 kmph")
car1=car("ford")
bike1=bike("gjgj")
car1.max_speed()
bike1.max_speed()
        