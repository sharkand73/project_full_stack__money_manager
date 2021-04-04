import unittest

from money_manager.models.merchant import Merchant
from money_manager.models.tag import Tag
from money_manager.models.transaction import Transaction
from datetime import datetime

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.tag_1 = Tag("Groceries")
        self.tag_2 = Tag("Entertainment")
        self.merchant_1 = Merchant("Tesco")
        self.merchant_2 = Merchant("Odeon Cinemas")
        self.date_1 = datetime(2021, 3, 31)
        self.transaction_1 = Transaction(self.date_1, self.merchant_1, 32.50, self.tag_1)
        self.transaction_2 = Transaction(self.date_1, self.merchant_2, 15.00, self.tag_2)

    def test_transaction_has_date(self):
        self.assertEqual("31-03-2021", self.transaction_1.date.strftime("%d-%m-%Y"))

    def test_transaction_has_merchant(self):
        self.assertEqual("Tesco", self.transaction_1.merchant.name)

    def test_transaction_has_tag(self):
        self.assertEqual("Entertainment", self.transaction_2.tag.category)

    def test_transaction_has_amount(self):
        self.assertEqual(32.50, self.transaction_1.amount)

    def test_transaction_id_is_None(self):
        self.assertIsNone(self.transaction_1.id)
