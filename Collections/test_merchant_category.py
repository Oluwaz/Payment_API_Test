import pytest
from test_token_generation import token
import requests


base_url = "https://developer.ecobank.com"

def test_merchant():
    payload = {
        "requestId": "123344",
        "affiliateCode": "EGH",
        "requestToken": "/4mZF42iofzo7BDu0YtbwY6swLwk46Z91xItybhYwQGFpaZNOpsznL/9fca5LkeV",
        "sourceCode": "ECOBANK_QR_API",
        "sourceChannelId": "KANZAN",
        "requestType": "CREATE_MERCHANT"
    }
    headers = {
        "Content-Type": "application/json",
        "Origin": "developer.ecobank.com",
        "Authorization": f"Bearer {token}"
    }

    request = requests.post(base_url + "/corporateapi/merchant/getmcc", json=payload, headers=headers)
    assert request.status_code == 200
