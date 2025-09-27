from typing import Optional, List
from uuid import uuid4

from app.entities.menu_item import MenuItem

class Restaurant:
    def __init__(self, name: str, location: str, restaurant_id: Optional[str] = None):
        self.restaurant_id = restaurant_id if restaurant_id else str(uuid4())
        self.name = name
        self.location = location
        self.menu: List[MenuItem] = []  # List of MenuItem objects




    # --- Menu Operations ---
    def add_item(self, item: MenuItem) -> str:
        """Add new item to menu if not already present."""
        for menu_item in self.menu:
            if menu_item.name == item.name:
                return "Item already exists in the menu"
        self.menu.append(item)
        return "Item added successfully"

    def remove_item(self, item_id: str) -> str:
        """Remove an item from the menu by ID."""
        for menu_item in self.menu:
            if menu_item.item_id == item_id:
                self.menu.remove(menu_item)
                return "Item removed successfully"
        return "Item not found"

    def mark_item_unavailable(self, item_id: str) -> str:
        for menu_item in self.menu:
            if menu_item.item_id == item_id:
                menu_item.mark_unavailable()
                return "Item marked as unavailable"
        return "Item not found"

    def mark_item_available(self, item_id: str) -> str:
        for menu_item in self.menu:
            if menu_item.item_id == item_id:
                menu_item.mark_available()
                return "Item marked as available"
        return "Item not found"

    def list_available_items(self) -> List[MenuItem]:
        """Return only items that are currently available."""
        return [item for item in self.menu if item.available]
