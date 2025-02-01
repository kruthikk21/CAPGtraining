class payment:
    def __init__(self,amount):
        self.amount=amount
    

    def pay(self):
        
        print("Payment of amount", self.amount, "is successful")
class creditcard(payment):
    def pay(self):
        print(f"Payment of amount {self.amount} through credit card is successful")
class paypal(payment,):
    def pay(self):
        print(f"Payment of amount{self.amount} through paypal is successful")
class bitcoin_payment(payment):
    def pay(self):
        print(f"Payment of amount{self.amount} through bitcoin is successful")
obj1=creditcard(200)
obj2=paypal(450)
obj3=bitcoin_payment(346)
obj1.pay()
obj2.pay()
obj3.pay()

