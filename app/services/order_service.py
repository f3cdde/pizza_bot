from app.models import Order

class OrderService:
    def __init__(self):
        self.orders = []

    def create_order(self, customer_name, customer_phone, pizza_type, quantity, address):
        order = Order(customer_name, customer_phone, pizza_type, quantity, address)
        self.orders.append(order)
        return order

    def get_orders(self):
        return self.orders
