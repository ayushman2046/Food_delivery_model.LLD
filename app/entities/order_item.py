from uuid import uuid4

class OrderItem:
    def __init__(self, item_id: str, name: str, price: float, quantity: int = 1):
        self.order_item_id = str(uuid4())
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} x {self.quantity} = ${self.total_price():.2f}"
