from enum import Enum
from abc import ABC, abstractmethod
from uuid import uuid4
from datetime import datetime, timedelta
from typing import List, Optional

from app.entities.order_item import OrderItem


class State(Enum):
    PENDING = "PENDING"
    DELIVERED = "DELIVERED"
    PLACED = "PLACED"
    ACCEPTED = "ACCEPTED"
    IN_PROGRESS = "IN PROGRESS"
    DISPATCHED  = "OUT FOR DELIVERY"



class OrderState(ABC):
    @abstractmethod
    def next_state(self, order):
        pass



class PlacedState(OrderState):
    def next_state(self, order):
        order.set_state(AcceptedState())

    def __str__(self):
        return "PLACED"


class AcceptedState(OrderState):
    def next_state(self, order):
        order.set_state(DispatchedState())

    def __str__(self):
        return "ACCEPTED"


class DispatchedState(OrderState):
    def next_state(self, order):
        order.set_state(DeliveredState())

    def __str__(self):
        return "DISPATCHED"


class DeliveredState(OrderState):
    def next_state(self, order):
        raise Exception("Order already delivered. Cannot change state further.")

    def __str__(self):
        return "DELIVERED"





class Order:
    def __init__(self, user_id: str, restaurant_id: str, items: List[OrderItem], order_id: Optional[str] = None):
        self.order_id = order_id if order_id else str(uuid4())
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.items = items
        self.created_at = datetime.now()
        self.estimated_delivery_time = self.created_at + timedelta(minutes=30)  # Default ETA
        self.state: OrderState = PlacedState()  # Initial state
        self.total_price = self.calculate_total()

    # --- Private Methods ---
    def calculate_total(self):
        return sum(item.total_price() for item in self.items)

    # --- State Management ---
    def set_state(self, new_state: OrderState):
        self.state = new_state

    def move_to_next_state(self):
        self.state.next_state(self)

    # --- Utility Methods ---
    def summary(self):
        items_summary = "\n".join(str(item) for item in self.items)
        return (
            f"Order ID: {self.order_id}\n"
            f"User ID: {self.user_id}\n"
            f"Restaurant ID: {self.restaurant_id}\n"
            f"Status: {self.state}\n"
            f"Total Price: ${self.total_price:.2f}\n"
            f"Items:\n{items_summary}\n"
            f"Estimated Delivery: {self.estimated_delivery_time}"
        )

    

