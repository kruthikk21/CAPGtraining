class car:
    def mode_of_transport(self):
        print("the car travels on road")
class airplane:
    def mode_of_transport(self):
        print("airplane travels in air")
class Flying_car(car,airplane):
    def mode_of_transport(self):
        print("flying car can travel on road and in air")
obj=Flying_car()
obj.mode_of_transport()