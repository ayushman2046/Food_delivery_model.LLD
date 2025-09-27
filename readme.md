

```
Functional Requirements:
    1. User should be able to order food.
    2. User should be able to browse the restaurant and check the foods and search.
    3. User should be able to track the order (PLACED -> ACCEPTED -> IN PROGRESS -> DISPATCHED -> DELIVERED)
    4. Restaurant owner should be able to update the menu and add/ remove the items.

Non Functional Requirements:
    1. System should be highly scalable as millions of users can order at a time.
    2. System should be able to maintain the order (shouldn't lost in any cases).

```

```
Entities:
    1. User
    2. Restaurant
    3. Order
    4. Menu
    5. OrderItem
    6. Payment
```

```
DB design:
    1. User:
        a. user_id : ObjectId
        b. name : str
        c. address : str
        d. phone_number : str
    2. Order:
        a. State : Enum
        b. items : List[item]
        c. price : int
        d. estimated time of delivery : Datetime
        e. order_id : int
        f. user_id : ObjectId
        g. restaurant_id : int
    3. Restaurant:
        a. restaurant_id : int
        b. menu
        c. items_available : boolean
        d. location : str
        e. name: str
    4. Menu:
        a. menu_id
        b. OrderItems : List
        c. name
    5. Payment:
        a. payment_id : int
        b. amount : int
        c. failed/succeed (Might be) : str
        d. order_id : int
    
    6. OrderItem:
        a. item_name
        b. price
        c. isavailable
```

```
Flow:
    -> User places an order → order saved in DB → state = PLACED.
    -> Restaurant accepts the order → state = ACCEPTED.
    -> Delivery partner picks it → state = DISPATCHED.
    -> Payment confirmed → state = DELIVERED.
```
