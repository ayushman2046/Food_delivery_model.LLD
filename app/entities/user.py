
from typing import Optional


class user:
    def __init__(self, name, address, phone_number, user_id : Optional[str]=None):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.user_id = user_id
        self.orders_list = []
    
    def place_order(self, order_id):
        self.orders_list.append(order_id)