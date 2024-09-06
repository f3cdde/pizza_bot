class Order:
    def __init__(self, customer_name, customer_phone, pizza_type, quantity, address):
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.pizza_type = pizza_type
        self.quantity = quantity
        self.address = address

class Menu:
    def __init__(self):
        self.items = {
            "Margherita": 10.0,
            "Pepperoni": 12.0,
            "Hawaiian": 11.0,
            "Veggie": 9.0
        }
