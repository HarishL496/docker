import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Temperature Converter" in response.data

def test_c_to_f(client):
    response = client.get('/convert/c-to-f?celsius=100')
    assert response.status_code == 200
    assert response.json['fahrenheit'] == 212.0
