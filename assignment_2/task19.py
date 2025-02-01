from abc import ABC, abstractmethod
class Ivehicle:
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class car(Ivehicle):
    def start_engine(self):
        print("car engine started")
    def stop_engine(self):
        print("car engine stopped")
class bike(Ivehicle):
    def start_engine(self):
        print("bike engine started")
    def stop_engine(self):
        print("bike engine stopped")
class truck(Ivehicle):
    def start_engine(self):
        print("truck engine started")
    def stop_engine(self):
        print("truck engine stopped")
obj1=car()
obj1.start_engine()
obj1.stop_engine()
obj2=bike()
obj2.start_engine()
obj2.stop_engine()
obj3=truck()
obj3.start_engine()
obj3.stop_engine()
