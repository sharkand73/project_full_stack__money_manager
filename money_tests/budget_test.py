import unittest
from datetime import datetime
from money_manager.models.budget import Budget

class TestBudget(unittest.TestCase):
    def setUp(self):
        date_1 = datetime(2021,3,1)
        date_2 = datetime(2021,3,31)
        self.budget_1 = Budget("March 2021", date_1, date_2, 1000)

    def test_budget_has_name(self):
        self.assertEqual("March 2021", self.budget_1.name)

    def test_budget_has_start_date(self):
        self.assertEqual("01-03-2021", self.budget_1.start_date.strftime("%d-%m-%Y"))

    def test_budget_has_end_date(self):
        self.assertEqual("31-03-2021", self.budget_1.end_date.strftime("%d-%m-%Y"))

    def test_budget_has_amount(self):
        self.assertEqual(1000, self.budget_1.amount)

    def test_budget_time_period(self):
        time_period = self.budget_1.time_period()
        self.assertEqual(31, time_period)