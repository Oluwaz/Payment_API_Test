import requests
import pytest

base_url = "https://developer.ecobank.com"



def test_qr_payment(token):
    payload = {
    "headerRequest": {
        "requestId": "",
        "affiliateCode": "EGH",
        "requestToken": "/4mZF42iofzo7BDu0YtbwY6swLwk46Z91xItybhYwQGFpaZNOpsznL/9fca5LkeV",
        "sourceCode": "ECOBANK_QR_API",
        "sourceChannelId": "KANZAN",
        "requestType":"CREATE_MERCHANT"
    },
    "merchantAddress": "123ERT",
    "merchantName":"UNIFIED SHOPPING CENTER",
    "accountNumber": "02002233444",
    "terminalName": "UNIFIED KIDS SHOPPING ARCADE",
    "mobileNumber": "0245293945",
    "email": "freemanst@gmail.com",
    "area": "Ridge",
    "city": "Ridge",
    "referralCode": "123456",
    "mcc": "0000",
    "dynamicQr":"Y",
    "callBackUrl":"http://koala.php",
    "secure_hash":"7f137705f4caa39dd691e771403430dd23d27aa53cefcb97217927312e77847bca6b8764f487ce5d1f6520fd7227e4d4c470c5d1e7455822c8ee95b10a0e9855"
}
    
    headers = {
        "Content-Type": "application/json",
        "Origin": "developer.ecobank.com",
        "Authorization": f"Bearer {token}"
    }
    request = requests.post(base_url + "/corporateapi/merchant/createqr", json=payload, headers=headers)

    assert request.status_code == 200
    load = request.json()

    print(load)

