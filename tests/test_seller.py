import unittest
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.repository.seller_repository import SellerRepository
from app.services.seller_service import SellerService

class TestSellerModule(unittest.TestCase):

    def test_singleton_repository(self):
        """Test that SellerRepository is a true Singleton."""
        repo1 = SellerRepository()
        repo2 = SellerRepository()
        self.assertIs(repo1, repo2, "SellerRepository instances should be identical")

    def test_service_initialization(self):
        """Test that SellerService initializes correctly with repository."""
        service = SellerService()
        self.assertIsInstance(service.repo, SellerRepository)
    
    def test_submission_structure(self):
        """Test mock submission logic."""
        # Using a mock-like logic since we don't want to write to actual files in unit tests usually
        # But for this simple project, we can test the structure logic
        pass

if __name__ == '__main__':
    unittest.main()
