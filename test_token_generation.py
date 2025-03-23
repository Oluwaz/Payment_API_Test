import requests
import pytest


base_url = "https://developer.ecobank.com"
lab_key = "0C/5F7QHdMv40uVGaTbt5nXdJOxi105k2LN9goPRqTUrwZrdYOYbvC0sJz7G0iT9"


def test_token_generation():

    payload = {
    "userId": "iamaunifieddev103",
    "password": "$2a$10$Wmame.Lh1FJDCB4JJIxtx.3SZT0dP2XlQWgj9Q5UAGcDLpB0yRYCC"
    }
    headers = {
        "Authorization": f"Bearer {lab_key}",
        "Content-Type": "application/json"
    }

    request = requests.post(base_url + "/corporateapi/user/token", json=payload, headers=headers)
    assert request.status_code == 200

