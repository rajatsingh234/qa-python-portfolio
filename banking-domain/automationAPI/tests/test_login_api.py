import requests
from automationAPI.config.config import USERNAME, PASSWORD, LOGIN_URL


def test_login_api():
    payload = {
        "username": USERNAME,
        "password": PASSWORD,
    }
    response = requests.post(LOGIN_URL, data=payload)

    #validate response
    assert response.status_code == 200
    print(response.json())

    # Validate session is created
    assert "JSESSIONID" in response.cookies
