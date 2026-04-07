class Inventory:
    def __init__(self):
        self.stock = {}

    def add_item(self, name, qty):
        self.stock[name] = self.stock.get(name, 0) + qty

    def remove_item(self, name, qty):
        if name in self.stock:
            self.stock[name] -= qty
