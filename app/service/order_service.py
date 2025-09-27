from typing import List
from datetime import datetime

from app.entities.menu_item import MenuItem
from app.entities.order import Order
from app.entities.order_item import OrderItem


class OrderService:
    def __init__(self, user_repo, restaurant_repo, order_repo):
        self.user_repo = user_repo
        self.restaurant_repo = restaurant_repo
        self.order_repo = order_repo

    def create_order(self, user_id: str, restaurant_id: str, items: List[dict]):
        # 1. Validate User
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise Exception("User not found")

        # 2. Validate Restaurant
        restaurant = self.restaurant_repo.find_by_id(restaurant_id)
        if not restaurant:
            raise Exception("Restaurant not found")

        # 3. Validate Items & Create OrderItems
        order_items = []
        for item_req in items:
            item_name = item_req["name"]
            quantity = item_req.get("quantity", 1)

            menu_item = next((item for item in restaurant.menu if item.name == item_name and item.available), None)
            if not menu_item:
                raise Exception(f"Item '{item_name}' not available")

            order_item = OrderItem(item_id=menu_item.item_id, name=menu_item.name, price=menu_item.price, quantity=quantity)
            order_items.append(order_item)

        # 4. Create Order
        order = Order(user_id=user_id, restaurant_id=restaurant_id, items=order_items)
        self.order_repo.save(order)

        # 5. Link Order to User
        user.place_order(order.order_id)

        return order

    def update_order_state(self, order_id: str):
        order = self.order_repo.find_by_id(order_id)
        if not order:
            raise Exception("Order not found")

        order.move_to_next_state()
        return order

    def get_order_summary(self, order_id: str):
        order = self.order_repo.find_by_id(order_id)
        if not order:
            raise Exception("Order not found")

        return order.summary()


