from typing import Optional
from uuid import uuid4

class MenuItem:
    def __init__(self, name: str, price: float, available: bool = True, item_id: Optional[str] = None):
        self.item_id = item_id if item_id else str(uuid4())
        self.name = name
        self.price = price
        self.available = available

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True

    def __str__(self):
        return f"{self.name} (${self.price}) - {'Available' if self.available else 'Unavailable'}"
