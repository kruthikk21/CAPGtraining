from abc import ABC , abstractmethod
class userAuthentication:
    @abstractmethod
    def login(self):
        pass
    def logout(self):
        pass
class google:
    def login(self):
        print("login through google")
    def logout(self):
        print("logout from google")
class facebookAuth:
    def login(self):
        print("login on facebook")
    def logout(self):
        print("logout from facebook")
obj=google()
obj.login()
obj.logout()
obj1=facebookAuth()
obj1.login()
obj1.logout()
