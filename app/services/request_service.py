from app.repository.approved_repository import ApprovedRepository
from app.repository.request_repository import RequestRepository
from app.repository.rejected_repository import RejectedRepository
from app.repository.product_repository import ProductRepository


class RequestService:
    def __init__(self):
        self.request_repo = RequestRepository()
        self.approved_repo = ApprovedRepository()
        self.rejected_repo = RejectedRepository()

    def approve(self, request_id):
        item = self.request_repo.remove_by_id(request_id)
        if not item:
            raise ValueError("Request not found")

        item["status"] = "approved"
        self.approved_repo.add(item)

    def reject(self, request_id):
        item = self.request_repo.remove_by_id(request_id)
        if not item:
            raise ValueError("Request not found")

        item["status"] = "rejected"
        self.rejected_repo.add(item)

    def __init__(self):
        self.request_repo = RequestRepository()
        self.product_repo = ProductRepository()
        self.rejected_repo = RejectedRepository()

    def approve(self, request_id):
        item = self.request_repo.remove_by_id(request_id)
        if not item:
            raise ValueError("Request not found")

        item["status"] = "approved"
        self.product_repo.add(item)

    def reject(self, request_id):
        item = self.request_repo.remove_by_id(request_id)
        if not item:
            raise ValueError("Request not found")

        item["status"] = "rejected"
        self.rejected_repo.add(item)
        
