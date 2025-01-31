from abc import ABC, abstractmethod
class father(ABC):
    @abstractmethod
    def profession(self):
        pass
    def introduce(self):
        self.profession()

class engineer(father):
    def profession(self):
        print("I am an engineer")
class doctor(father):
    def profession(self):
        print("I am a doctor")
enginner2=engineer()
enginner2.introduce()
doctor2=doctor()
doctor2.introduce()
