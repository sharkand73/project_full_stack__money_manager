import unittest

from money_manager.models.merchant import Merchant
from money_manager.models.tag import Tag
from money_manager.models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.tag_1 = Tag("Groceries")
        self.tag_2 = Tag("Entertainment")
        self.merchant_1 = Merchant("Tesco")
        self.merchant_2 = Merchant("Odeon Cinemas")
        self.transaction_1 = Transaction(self.merchant_1, self.tag_1, 32.50)
        self.transaction_2 = Transaction(self.merchant_2, self.tag_2, 15.00)

    def test_transaction_has_merchant(self):
        self.assertEqual("Tesco", self.transaction_1.merchant.name)

    def test_transaction_has_tag(self):
        self.assertEqual("Entertainment", self.transaction_2.tag.category)

    def test_transaction_has_amount(self):
        self.assertEqual(32.50, self.transaction_1.amount)

    def test_transaction_id_is_None(self):
        self.assertIsNone(self.transaction_1.id)
