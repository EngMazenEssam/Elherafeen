import sys
import os
import pytest
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

@patch('app.controllers.cart_controller.add_to_cart')
def test_add_to_cart_api(mock_service_add, client):
    mock_service_add.return_value = (True, None, 200)
    response = client.post('/cart/add', json={
        "oem": "123-TEST",
        "quantity": 5
    })
    
    assert response.status_code == 200
    assert response.json["ok"]
    
    mock_service_add.assert_called_once_with("123-TEST", 5)

@patch('app.controllers.cart_controller.add_to_cart')
def test_add_to_cart_api_missing_data(mock_service_add, client):
    response = client.post('/cart/add', json={"quantity": 1})
    assert response.status_code == 400
    assert not response.json["ok"]
    assert "Missing OEM" in response.json["error"]
