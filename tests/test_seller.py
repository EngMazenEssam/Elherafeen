import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.repository.seller_repository import SellerRepository
from app.services.seller_service import SellerService

class TestSellerModule(unittest.TestCase):

    def test_singleton_repository(self):
        repo1 = SellerRepository()
        repo2 = SellerRepository()
        self.assertIs(repo1, repo2, "SellerRepository instances should be identical")

    def test_service_initialization(self):
        service = SellerService()
        self.assertIsInstance(service.repo, SellerRepository)
    
    def test_submission_structure(self):

        pass

if __name__ == '__main__':
    unittest.main()
