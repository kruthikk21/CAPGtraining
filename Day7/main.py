from order import Order 


order1 = Order(
    cust_id=101, password="pass123", first_name="John", last_name="Doe",
    phone="1234567890", email="john@example.com", city="New York", state="NY", zip_code="10001",
    order_id=5001, order_status="Shipped", ordered_date="2025-01-25",
    required_date="2025-02-01", shipped_date="2025-01-28", store_id=10, staff_id=3
)


order1.display()  
