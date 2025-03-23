import requests
import pytest


base_url = "https://developer.ecobank.com"
lab_key = "0C/5F7QHdMv40uVGaTbt5nXdJOxi105k2LN9goPRqTUrwZrdYOYbvC0sJz7G0iT9"


def test_token_generation():

    payload = {
    "userId": "iamaunifieddev103",
    "password": "$2a$10$Wmame.Lh1FJDCB4JJIxtx.3SZT0dP2XlQWgj9Q5UAGcDLpB0yRYCC"
    }
    #headers = {
    #    "Authorization": f"Bearer {lab_key}",
    #    "Content-Type": "application/json",
    #   ### "Accept": "application/json",
    #    ##"Origin": "https://developer.ecobank.com"
    #}

    headers = {
        "Content-Type": "application/json",
        "Origin": "https://developer.ecobank.com",
        # Adjust authentication header based on API requirements
        # "Authorization": f"Bearer {lab_key}"  # If Bearer token is required
        # "X-API-Key": lab_key  # If API key is required in a different header
        # "X-Client-ID": "your_client_id",  # If client ID is needed
        # "X-Request-ID": "unique-uuid-here"  # For request tracking
    }


    request = requests.post(base_url + "/corporateapi/user/token", json=payload, headers=headers)
    assert request.status_code == 200