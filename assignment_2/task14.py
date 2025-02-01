class notification:
    def send(self):
        print("sending notification")
class email(notification):
    def send(self):
        print("sending email")
class sms_notification(notification):
    def send(self):
        print("sending sms")
obj=email()
obj2=sms_notification()
obj.send()
obj2.send()
