from customer import Customer  

class Order(Customer): 
    def __init__(self, cust_id, password, first_name, last_name, phone, email, city, state, zip_code,
                 order_id, order_status, ordered_date, required_date, shipped_date, store_id, staff_id):
       
        super().__init__(cust_id, password, first_name, last_name, phone, email, city, state, zip_code)
        
  
        self.order_id = order_id
        self.order_status = order_status
        self.ordered_date = ordered_date
        self.required_date = required_date
        self.shipped_date = shipped_date
        self.store_id = store_id
        self.staff_id = staff_id

    def display(self):
        print(f"Order ID: {self.order_id}, Customer ID: {self.cust_id}, Status: {self.order_status}, Ordered Date: {self.ordered_date}")
