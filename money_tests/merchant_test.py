import unittest

from money_manager.models.merchant import Merchant
#from money_manager.models.tag import Tag
#from money_manager.models.transaction import Transaction

class TestMerchant(unittest.TestCase):
    def setUp(self):
        self.merchant_1 = Merchant("Tesco", 1)
        self.merchant_2 = Merchant("Apple")

    def test_merchant_has_name(self):
        self.assertEqual("Tesco", self.merchant_1.name)
        self.assertEqual("Apple", self.merchant_2.name)

    def test_merchant_has_id(self):
        self.assertEqual(1, self.merchant_1.id)

    def test_merchant_id_is_None(self):
        self.assertIsNone(self.merchant_2.id)