import sys
import os
import pytest
from unittest.mock import patch, MagicMock

# This helps Python find your app code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services import product_service
from app.services import cart_service
from app.services.user_service import UserService
from app.models.user import User

# --- Product Service Tests ---

def test_build_product_object():
    """Test that we can create a nice product dictionary"""
    seller = {"name": "Test Seller"}
    product_data = {"oem": "123", "price": 100}
    seller_id = "s1"
    
    result = product_service.build_product_object(seller_id, seller, product_data)
    
    assert result["seller_name"] == "Test Seller"
    assert result["id"] == "s1_123"
    assert result["oem"] == "123"

@patch('app.services.product_service.get_all_products')
def test_search_for_product(mock_get_all):
    """Test searching for a product by name"""
    # Fake data so we don't need real files
    mock_get_all.return_value = [
        {"name": "Brake Pad", "oem": "BP001", "category": "Brakes"},
        {"name": "Oil Filter", "oem": "OF001", "category": "Filters"},
        {"name": "Water Pump", "oem": "WP999", "category": "Cooling"}
    ]
    
    # Test 1: Search for "Brake"
    results = product_service.filter_products(search="Brake")
    assert len(results) == 1
    assert results[0]["oem"] == "BP001"

    # Test 2: Search for "water" (case insensitive)
    results = product_service.filter_products(search="water")
    assert len(results) == 1
    assert results[0]["oem"] == "WP999"

@patch('app.services.product_service.iter_all_products')
def test_get_product_by_id(mock_iter):
    """Test finding a specific product by its ID"""
    # ID format is sellerID_oem
    mock_iter.return_value = [
        ("s1", {"name": "Seller A"}, {"oem": "123", "name": "Item A"}),
        ("s2", {"name": "Seller B"}, {"oem": "456", "name": "Item B"})
    ]

    # Should find s1_123
    product = product_service.get_product_by_id("s1_123")
    assert product is not None
    assert product["name"] == "Item A"
    assert product["seller_name"] == "Seller A"

    # Should NOT find s99_999
    missing = product_service.get_product_by_id("s99_999")
    assert missing is None

# --- Cart Service Tests ---

@patch('app.services.cart_service.load_cart_raw')
@patch('app.services.cart_service.save_cart_raw')
def test_add_item_to_cart(mock_save, mock_load):
    """Test adding a new item to the cart"""
    # Start with an empty cart
    mock_load.return_value = {"items": []}
    
    success, msg, code = cart_service.add_to_cart("OEM123", 2)
    
    assert success == True
    assert code == 200
    
    # Check if save was called
    mock_save.assert_called_once()
    saved_data = mock_save.call_args[0][0]
    assert saved_data["items"][0]["oem"] == "OEM123"
    assert saved_data["items"][0]["quantity"] == 2

@patch('app.services.cart_service.load_cart_raw')
@patch('app.services.cart_service.save_cart_raw')
def test_remove_item_from_cart(mock_save, mock_load):
    """Test removing an item works"""
    # Start with one item in cart
    mock_load.return_value = {"items": [{"oem": "OEM123", "quantity": 1}]}
    
    success, msg, code = cart_service.remove_from_cart("OEM123")
    
    assert success == True
    
    # Check that we saved an empty list (item removed)
    saved_data = mock_save.call_args[0][0]
    assert len(saved_data["items"]) == 0

@patch('app.services.cart_service.load_cart_raw')
@patch('app.services.cart_service.save_cart_raw')
def test_update_item_quantity(mock_save, mock_load):
    """Test changing the quantity of an item"""
    # Start with quantity 1
    mock_load.return_value = {"items": [{"oem": "OEM123", "quantity": 1}]}
    
    success, msg, code = cart_service.update_cart_quantity("OEM123", 5)
    
    assert success == True
    
    saved_data = mock_save.call_args[0][0]
    assert saved_data["items"][0]["quantity"] == 5

@patch('app.services.cart_service.load_cart_raw')
@patch('app.services.cart_service.load_products_raw')
def test_cart_totals_calculation(mock_load_products, mock_load_cart):
    """Test that the total price is calculated correctly"""
    # Fake cart: 2 items of 'OEM1'
    mock_load_cart.return_value = {"items": [{"oem": "OEM1", "quantity": 2}]}
    
    # Fake product database
    mock_load_products.return_value = {
        "s1": {
            "name": "Seller 1",
            "products": [{"oem": "OEM1", "price": 10}]
        }
    }
    
    items, subtotal, total_qty = cart_service.get_cart_items_with_totals()
    
    assert subtotal == 20 # 2 * 10
    assert total_qty == 2

# --- User Service Tests ---

def test_register_user_success():
    """Test registering a user successfully"""
    # Mock the repository so we don't write to real files
    mock_repo = MagicMock()
    # Assume email doesn't exist yet
    mock_repo.find_by_email.return_value = None
    
    service = UserService(repo=mock_repo)
    
    user = service.register_user(
        fullname="Ali Test",
        email="ali@test.com",
        phone="123456",
        password="secretpassword",
        confirm="secretpassword"
    )
    
    assert user.email == "ali@test.com"
    assert user.fullname == "Ali Test"
    # Essential: Verify we called add_user on the repo
    mock_repo.add_user.assert_called_once()

def test_register_user_password_mismatch():
    """Test registration fails if passwords don't match"""
    mock_repo = MagicMock()
    service = UserService(repo=mock_repo)
    
    # Should raise value error
    with pytest.raises(ValueError) as excinfo:
        service.register_user(
            fullname="Test",
            email="test@test.com",
            phone="123",
            password="passA",
            confirm="passB" # Mismatch
        )
    
    assert "Passwords do not match" in str(excinfo.value)

def test_login_user_success():
    """Test logging in with correct password"""
    mock_repo = MagicMock()
    service = UserService(repo=mock_repo)
    
    # Create a fake user that already exists in "database"
    # We must start with a known hash. 
    # Let's use the service's internal helper to make a valid hash for 'mypass'
    real_password = "mypass"
    hashed_pw = service._hash_password(real_password)
    
    existing_user = User(
        id="u1", 
        fullname="Test User", 
        email="login@test.com", 
        phone="111", 
        password_hash=hashed_pw
    )
    
    mock_repo.find_by_email.return_value = existing_user
    
    # Try to login
    logged_in_user = service.login_user("login@test.com", real_password)
    
    assert logged_in_user is not None
    assert logged_in_user.email == "login@test.com"

def test_login_user_wrong_password():
    """Test login fails with wrong password"""
    mock_repo = MagicMock()
    service = UserService(repo=mock_repo)
    
    real_password = "correct"
    hashed_pw = service._hash_password(real_password)
    
    existing_user = User(
        id="u1", fullname="Test", email="test@test.com", phone="1", password_hash=hashed_pw
    )
    mock_repo.find_by_email.return_value = existing_user
    
    with pytest.raises(ValueError) as excinfo:
        service.login_user("test@test.com", "WRONG")
    
    assert "Invalid email or password" in str(excinfo.value)
