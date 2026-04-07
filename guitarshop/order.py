class Order():
    def __init__(self):
        self.items = []
    def add_item(self, product, quantity):
        self.items.append((product, quantity))
        product.hold += 1

    def get_items(self):
        return self.items