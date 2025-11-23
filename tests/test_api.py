import os
import requests

BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')

def test_healthcheck():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200

def test_create_account():
    payload = {
        "name": "Test User",
        "email": "test.user@example.com",
        "initial_deposit": 100.0
    }
    r = requests.post(f"{BASE_URL}/api/accounts", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data.get('account_id') is not None
