from app.repository.product_moderation_repository import ProductModerationRepository


class ProductModerationService:
    def __init__(self):
        self.repo = ProductModerationRepository()

    def get_pending_products(self):
        return self.repo.get_pending()

    def approve(self, product_id):
        self.repo.approve(product_id)

    def reject(self, product_id):
        self.repo.reject(product_id)