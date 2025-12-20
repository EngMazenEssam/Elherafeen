import sys
import os

# Add project root to path
sys.path.append(os.getcwd())

from app.services.seller_service import SellerService

# Mock request data
form_data = {
    "brand": "Lamborghini",
    "model": "Aventador",
    "year": "2024",
    "condition": "New",
    "price": "500000",
    "currency": "USD",
    "description": "Test submission from script"
}

files = {} # No files for this test

service = SellerService()
try:
    print("Submitting product...")
    product = service.submit_product(form_data, files, "seller_test_1")
    print(f"Product submitted with ID: {product['id']}")
    
    # Check pending
    data = service.get_dashboard_data("seller_test_1")
    pending = data["pending"]
    print(f"Pending items for seller: {len(pending)}")
    
    found = any(p['id'] == product['id'] for p in pending)
    if found:
        print("SUCCESS: Product found in pending list.")
    else:
        print("FAILURE: Product not found in pending list.")

except Exception as e:
    print(f"ERROR: {e}")
