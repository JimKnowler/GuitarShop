import unittest

class Order():
    def __init__(self):
        self.items = []
    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def get_items(self):
        return self.items

class Product():
    def __init__(self, id, stock, hold):
        self.id = id
        self.stock = stock
        self.hold = hold

class TestClass(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(1, 1)

    def test_new_item_added_to_order(self):
        order = Order()
        product = Product(327,7,0)
        order.add_item(product, 1)
        order_items = order.get_items()
        self.assertEqual(order_items,[(product,1)])