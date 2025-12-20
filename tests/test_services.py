import sys
import os
import pytest
from unittest.mock import patch, MagicMock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services import product_service, cart_service
from app.services.user_service import UserService
from app.models.user import User
def test_build_product_object():
    seller = {"name": "Test Seller"}
    product_data = {"oem": "123", "price": 100}
    seller_id = "s1"
    
    result = product_service.build_product_object(seller_id, seller, product_data)
    
    assert result["seller_name"] == "Test Seller"
    assert result["id"] == "s1_123"
    assert result["oem"] == "123"

@patch('app.services.product_service.get_all_products')
def test_search_for_product(mock_get_all):
    mock_get_all.return_value = [
        {"name": "Brake Pad", "oem": "BP001", "category": "Brakes"},{"name": "Oil Filter", "oem": "OF001", "category": "Filters"},{"name": "Water Pump", "oem": "WP999", "category": "Cooling"}]
    results = product_service.filter_products(search="Brake")
    assert len(results) == 1
    assert results[0]["oem"] == "BP001"
    results = product_service.filter_products(search="water")
    assert len(results) == 1
    assert results[0]["oem"] == "WP999"

@patch('app.services.product_service.iter_all_products')
def test_get_product_by_id(mock_iter):
    mock_iter.return_value = [
        ("s1", {"name": "Seller A"}, {"oem": "123", "name": "Item A"}),
        ("s2", {"name": "Seller B"}, {"oem": "456", "name": "Item B"})
    ]
    product = product_service.get_product_by_id("s1_123")
    assert product is not None
    assert product["name"] == "Item A"
    assert product["seller_name"] == "Seller A"
    missing = product_service.get_product_by_id("s99_999")
    assert missing is None

@patch('app.services.cart_service.load_cart_raw')
@patch('app.services.cart_service.save_cart_raw')
def test_add_item_to_cart(mock_save, mock_load):
    mock_load.return_value = {"items": []}
    
    success, msg, code = cart_service.add_to_cart("OEM123", 2)
    
    assert success
    assert code == 200
    
    mock_save.assert_called_once()
    saved_data = mock_save.call_args[0][0]
    assert saved_data["items"][0]["oem"] == "OEM123"
    assert saved_data["items"][0]["quantity"] == 2

@patch('app.services.cart_service.load_cart_raw')
@patch('app.services.cart_service.save_cart_raw')
def test_remove_item_from_cart(mock_save, mock_load):
    mock_load.return_value = {"items": [{"oem": "OEM123", "quantity": 1}]}
    
    success, msg, code = cart_service.remove_from_cart("OEM123")
    
    assert success
    saved_data = mock_save.call_args[0][0]
    assert len(saved_data["items"]) == 0

@patch('app.services.cart_service.load_cart_raw')
@patch('app.services.cart_service.save_cart_raw')
def test_update_item_quantity(mock_save, mock_load):
    mock_load.return_value = {"items": [{"oem": "OEM123", "quantity": 1}]}
    
    success, msg, code = cart_service.update_cart_quantity("OEM123", 5)
    
    assert success
    
    saved_data = mock_save.call_args[0][0]
    assert saved_data["items"][0]["quantity"] == 5

@patch('app.services.cart_service.load_cart_raw')
@patch('app.services.cart_service.load_products_raw')
def test_cart_totals_calculation(mock_load_products, mock_load_cart):
    mock_load_cart.return_value = {"items": [{"oem": "OEM1", "quantity": 2}]}
    mock_load_products.return_value = {
        "s1": {
            "name": "Seller 1",
            "products": [{"oem": "OEM1", "price": 10}]
        }
    }
    
    items, subtotal, total_qty = cart_service.get_cart_items_with_totals()
    
    assert subtotal == 20
    assert total_qty == 2

def test_register_user_success():
    mock_repo = MagicMock()
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
    mock_repo.add_user.assert_called_once()

def test_register_user_password_mismatch():
    mock_repo = MagicMock()
    service = UserService(repo=mock_repo)
    
    with pytest.raises(ValueError) as excinfo:
        service.register_user(
            fullname="Test",
            email="test@test.com",
            phone="123",
            password="passA",
            confirm="passB"
        )
    
    assert "Passwords do not match" in str(excinfo.value)

def test_login_user_success():
    mock_repo = MagicMock()
    service = UserService(repo=mock_repo)

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
    
    logged_in_user = service.login_user("login@test.com", real_password)
    
    assert logged_in_user is not None
    assert logged_in_user.email == "login@test.com"

def test_login_user_wrong_password():
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
