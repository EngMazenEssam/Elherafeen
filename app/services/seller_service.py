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
        """
        Processes the form submission.
        1. Saves images/videos if present.
        2. Constructs the product dictionary.
        3. Saves to pending.json via repository.
        """
        product_id = f"p-{uuid.uuid4().hex[:8]}"
        
        # Handle file upload
        image_filename = "default.jpg" # Placeholder
        if 'image' in files:
            file = files['image']
            if file and self._allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Unique name to prevent collision
                unique_name = f"{product_id}_{filename}"
                
                # Ensure directory exists
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                
                file_path = os.path.join(UPLOAD_FOLDER, unique_name)
                file.save(file_path)
                
                # Store relative path for frontend
                image_filename = f"products/{unique_name}"

        # Construct product data matching requirements
        product = {
            "id": product_id,
            "seller_id": seller_id,
            "status": "Pending",
            "submission_date": datetime.now().strftime("%Y-%m-%d"),
            "brand": form_data.get("brand"),
            "model": form_data.get("model"),
            "year": form_data.get("year"),
            "condition": form_data.get("condition"),
            "price": form_data.get("price"),
            "currency": form_data.get("currency", "EGP"),
            "description": form_data.get("description"),
            "image": image_filename,
            # Specs from the form
            "specs": {
                "engine_type": form_data.get("engine_type"),
                "horsepower": form_data.get("horsepower"),
                "transmission": form_data.get("transmission"),
                "drivetrain": form_data.get("drivetrain"),
                "fuel_type": form_data.get("fuel_type"),
                 # mileage or 0-60 could be added here
            }
        }

        self.repo.add_pending_product(product)
        return product

    def get_dashboard_data(self, seller_id):
        return {
            "pending": self.repo.get_pending_products(seller_id),
            "approved": self.repo.get_approved_products(seller_id)
        }
