class Customer:
    def __init__(self, cust_id, password, first_name, last_name, phone, email, city, state, zip_code):
        self.cust_id = cust_id
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def display(self):
        print(f"Customer ID: {self.cust_id}, Name: {self.first_name} {self.last_name}, City: {self.city}, State: {self.state}")
