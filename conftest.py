import requests
import pytest


base_url = "https://developer.ecobank.com"

@pytest.fixture
def token():
    payload = {
        "userId": "iamaunifieddev103",
        "password": "$2a$10$Wmame.Lh1FJDCB4JJIxtx.3SZT0dP2XlQWgj9Q5UAGcDLpB0yRYCC"
    }
    headers = {
        "Content-Type": "application/json",
        "Origin": "developer.ecobank.com",
        # Adjust authentication header based on API requirements
        # "Authorization": f"Bearer {lab_key}"  # If Bearer token is required
        # "X-API-Key": lab_key  # If API key is required in a different header
        # "X-Client-ID": "your_client_id",  # If client ID is needed
        # "X-Request-ID": "unique-uuid-here"  # For request tracking
    }
    request = requests.post(base_url + "/corporateapi/user/token", json=payload, headers=headers)
    assert request.status_code == 200
    assert request.json()["token"] is not None
    assert request.json()["token"] != ""
    token = request.json()["token"]
    return token

