from abc import ABC , abstractmethod
class mail(ABC):
    @abstractmethod
    def send(self):
        pass
class gmail(mail):
    def send(self):
        print("Sending mail using gmail")
class yahoo(mail):
    def send(self):
        print("Sending mail using yahoo")
class rediff(mail):
    def send(self):
        print("Sending mail using rediff")
class outlook(mail):
    def send(self):
        print("Sending mail using outlook")
g = gmail()
g.send()
y = yahoo()
y.send()
r = rediff()
r.send()
o = outlook()
o.send()
