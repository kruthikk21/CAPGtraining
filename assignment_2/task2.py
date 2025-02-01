class bank:
    def __init__(self):
        self.balance=0
    
    def deposit(self):
        amount=int(input("Enter the amount to deposit:"))
        self.balance+=amount
        print("Amount Deposited:",amount)
        
    
    def withdraw(self):
        amount=int(input("Enter the amount to withdraw:"))
        self.balance-=amount
        print("Amount Withdrawn:",amount)
    def get_balance(self):
        print("Balance:",self.balance)
obj=bank()
obj.deposit()
obj.withdraw()
obj.get_balance()