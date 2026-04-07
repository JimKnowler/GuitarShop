import unittest

from product import Product
from order import Order

class TestClass(unittest.TestCase):
    def test_new_item_added_to_order(self):
        order = Order()
        product = Product(327,7,0)
        order.add_item(product, 1)
        order_items = order.get_items()
        self.assertEqual(order_items,[(product,1)])

    def test_temporary_hold_placed_on_product(self):
        order = Order()
        product = Product(327,7,0)
        order.add_item(product, 1)
        self.assertEqual(product.hold, 1)

    def test_error_raised_if_insufficient_stock(self):
        with self.assertRaisesRegex(Exception, "Insufficient stock of Ibanez Tube Screamer. Only 1 currently available."):
            order = Order()
            product = Product(327,1,0, "Ibanez Tube Screamer")
            order.add_item(product, 2)