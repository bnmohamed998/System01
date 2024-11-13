import pytest
from app import app

def test_home():
    # Testing if the home page returns a 200 status code
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_calculate_add():
    with app.test_client() as client:
        response = client.post('/calculate', data={'x': '2', 'y': '3', 'operation': 'add'})
        assert response.status_code == 200
        assert response.json['result'] == 5

def test_calculate_subtract():
    with app.test_client() as client:
        response = client.post('/calculate', data={'x': '5', 'y': '3', 'operation': 'subtract'})
        assert response.status_code == 200
        assert response.json['result'] == 2

def test_calculate_multiply():
    with app.test_client() as client:
        response = client.post('/calculate', data={'x': '2', 'y': '3', 'operation': 'multiply'})
        assert response.status_code == 200
        assert response.json['result'] == 6

def test_calculate_divide():
    with app.test_client() as client:
        response = client.post('/calculate', data={'x': '6', 'y': '3', 'operation': 'divide'})
        assert response.status_code == 200
        assert response.json['result'] == 2.0
