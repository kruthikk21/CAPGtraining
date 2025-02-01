class electronics:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display(self):
        print("Name:",self.name)
        print("Price:",self.price)
class mobile(electronics):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand
    def display(self):
        super().display()
        print("Brand:",self.brand)
class smartphone(mobile):
    def __init__(self, name, price, brand, os):
        super().__init__(name, price, brand)
        self.os = os
    def display(self):
        super().display()
        print("OS:",self.os)
obj=smartphone("Iphone",50000,"Apple","iOS")
obj.display()

    


    