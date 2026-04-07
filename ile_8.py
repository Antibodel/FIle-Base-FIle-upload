import uuid

class OrderService:
    def __init__(self):
        self.orders = []

    def create_order(self, user_id, items):
        order_id = str(uuid.uuid4())
        order = {
            "id": order_id,
            "user": user_id,
            "items": items
        }
        self.orders.append(order)
        return order
