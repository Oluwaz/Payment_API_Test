import requests
import time

#from test_token_generation import test_token

import pytest

base_url = "https://developer.ecobank.com"

def test_card_payment(token):

    payload = {
    "paymentDetails": {
        "requestId": "0550342516521",
        "productCode": "2310",
        "amount": "30",
        "currency": "USD",
        "locale": "en_AU",
        "orderInfo": "b5f7f321d-9a4e-4c5c-a948-ab7642f43ce4",
        "returnUrl": "https://www.ecobank.com/unified"
    },
    "merchantDetails": {
        "accessCode": "31ba5746e7603385bc5c28c45710a4ec",
        "merchantID": "AE681FE1-FDB3-4477-B8A1-7553FE2099D7",
        "secureSecret": "38edcc440faa4637916b2fbdf4a5e02fbf807d9cce0e4404af741befe611cdf422a986eec5854660af42d06bd1c50f4d19ef35324bad47d7b9113f6daf5789cacd463bfa925d4bf3a93ca8cab15563cda375e428e4e740d290633fd6fce09e0bbb0fbfadb14147e0af91993266dfd0b6bc520aac868e49aca923cd332cc9a1a8"
    },
    "secureHash": "1be4bf59f4917a306005fd8178b8ae9ac385b832a94b15c7a87945cf374edab099e9735379833a01053c33f0edae94ebd0ffa8beb5680871e78c3b7630582331"
}
    headers = {
        "Content-Type": "application/json",
        "Origin": "developer.ecobank.com",
        "Authorization": f"Bearer {token}"
    }
    sart_time = time.time() 
    request = requests.post(base_url + "/corporateapi/merchant/Signature", json=payload, headers=headers)
    end_time = time.time( )

    time_taken = end_time - sart_time
    print(f"Time taken for request: {time_taken} seconds")

    assert request.status_code == 200
    assert time_taken < 2.0
    load = request.json()
    print(load)

    