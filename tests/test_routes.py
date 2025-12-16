import sys
import os
import pytest
from unittest.mock import patch, MagicMock

# Setup path to import from app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def client():
    """Create a test client for the app"""
    app = create_app()
    app.config['TESTING'] = True
    
    # Create test client
    with app.test_client() as client:
        yield client

def test_home_page_status_code(client):
    """Test that the home page returns a 200 OK status"""
    # Simply request the home page
    response = client.get('/')
    
    # Check that it succeeded
    assert response.status_code == 200
    # Check that it loads the correct template content (assuming "home.html" contains some HTML)
    # We can't check the exact HTML easily without viewing the template, 
    # but 200 is good enough for a basic route test.

@patch('app.controllers.cart_controller.add_to_cart')
def test_add_to_cart_api(mock_service_add, client):
    """Test the /cart/add API route"""
    # 1. Mock the service so we don't actually write to files
    mock_service_add.return_value = (True, None, 200)
    
    # 2. Make a POST request to add an item
    response = client.post('/cart/add', json={
        "oem": "123-TEST",
        "quantity": 5
    })
    
    # 3. Verify the response
    assert response.status_code == 200
    assert response.json["ok"] == True
    
    # 4. Verify the service was called with correct data
    mock_service_add.assert_called_once_with("123-TEST", 5)

@patch('app.controllers.cart_controller.add_to_cart')
def test_add_to_cart_api_missing_data(mock_service_add, client):
    """Test API handles missing data correctly"""
    # Make request without 'oem'
    response = client.post('/cart/add', json={
        "quantity": 1
    })
    
    assert response.status_code == 400
    assert response.json["ok"] == False
    assert "Missing OEM" in response.json["error"]
