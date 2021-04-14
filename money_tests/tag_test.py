import unittest

#from money_manager.models.merchant import Merchant
from money_manager.models.tag import Tag
#from money_manager.models.transaction import Transaction

class TestTag(unittest.TestCase):
    def setUp(self):
        self.tag_1 = Tag("Groceries")
        self.tag_2 = Tag("Clothes", 2)

    def test_tag_has_category(self):
        self.assertEqual("Groceries", self.tag_1.category)
        self.assertEqual("Clothes", self.tag_2.category)

    def test_tag_id_is_None(self):
        self.assertIsNone(self.tag_1.id)

    def test_tag_id(self):
        self.assertEqual(2, self.tag_2.id)

    

