import unittest
from core.contribution import ContributionHandler

class TestContributionHandler(unittest.TestCase):
    def setUp(self):
        self.handler = ContributionHandler(":memory:")

    def test_record_contribution(self):
        result = self.handler.record_contribution("user1", "data_upload", 100)
        self.assertEqual(result["status"], "success")

    def test_get_user_contributions(self):
        self.handler.record_contribution("user1", "data_upload", 100)
        contributions = self.handler.get_user_contributions("user1")
        self.assertEqual(len(contributions), 1)