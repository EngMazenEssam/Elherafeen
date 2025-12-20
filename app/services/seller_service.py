import os
import uuid
from datetime import datetime
from werkzeug.utils import secure_filename
from app.repository.seller_repository import SellerRepository

# Constants
UPLOAD_FOLDER = os.path.join("app", "static", "images", "products")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'mp4'}

class SellerService:
    def __init__(self):
        self.repo = SellerRepository()

    def _allowed_file(self, filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def submit_product(self, form_data, files, seller_id):
        product_id = f"p-{uuid.uuid4().hex[:8]}"
        
        # Handle file upload
        image_filename = "default.jpg"
        if 'image' in files:
            file = files['image']
            if file and self._allowed_file(file.filename):
                filename = secure_filename(file.filename)
                unique_name = f"{product_id}_{filename}"
                
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                
                file_path = os.path.join(UPLOAD_FOLDER, unique_name)
                file.save(file_path)
                
                image_filename = f"products/{unique_name}"

        # Process tags
        tags_input = form_data.get("tags", "")
        tags_list = [t.strip() for t in tags_input.split(",") if t.strip()]

        product = {
            "id": product_id,
            "seller_id": seller_id,
            "status": "Pending",
            "submission_date": datetime.now().strftime("%Y-%m-%d"),
            "name": form_data.get("name"),
            "category": form_data.get("category"),
            "type": form_data.get("type"),
            "brand": form_data.get("brand"),
            "condition": form_data.get("condition"),
            "price": form_data.get("price"),
            "currency": form_data.get("currency", "EGP"),
            "stock": int(form_data.get("stock")) if form_data.get("stock") else 0,
            "images": [image_filename],
            "description": form_data.get("description"),
            "sold_count": 0,
            "tags": tags_list
        }

        self.repo.add_pending_product(product)
        return product

    def get_dashboard_data(self, seller_id):
        return {
            "pending": self.repo.get_pending_products(seller_id),
            "approved": self.repo.get_approved_products(seller_id)
        }
