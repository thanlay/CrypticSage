import unittest
from core.dao import DAOManager

class TestDAOManager(unittest.TestCase):
    def setUp(self):
        self.dao = DAOManager()

    def test_create_proposal(self):
        result = self.dao.create_proposal("proposal_1", "Test Proposal")
        self.assertEqual(result["status"], "success")

    def test_duplicate_proposal(self):
        self.dao.create_proposal("proposal_1", "Test Proposal")
        result = self.dao.create_proposal("proposal_1", "Duplicate Proposal")
        self.assertEqual(result["status"], "failed")

    def test_vote_proposal(self):
        self.dao.create_proposal("proposal_1", "Test Proposal")
        result = self.dao.vote("proposal_1", "user_1", "yes")
        self.assertEqual(result["status"], "success")