class Order():
    def __init__(self):
        self.items = []
    def add_item(self, product, quantity):
        if product.stock - product.hold < quantity:
            raise Exception(f"Insufficient stock of {product.name}. Only {product.stock - product.hold} currently available.")
        self.items.append((product, quantity))
        product.hold += 1

    def get_items(self):
        return self.items