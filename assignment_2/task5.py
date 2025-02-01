class product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        self.quantity=input("Enter the quantity:")
    def check_availability(self):
        if int(self.quantity)<=self.stock:
            print("Available")
        else:
            print("Not Available")
obj=product("Laptop",50000,10)
obj.check_availability()
