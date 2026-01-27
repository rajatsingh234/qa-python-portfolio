import requests
import re
from automationAPI.config.config import USERNAME, PASSWORD, LOGIN_URL

OVERVIEW_URL = "https://parabank.parasoft.com/parabank/overview.htm"
BASE_URL = "https://parabank.parasoft.com/parabank"

def get_authenticated_session():
    '''
    You must be logged in
    You must use the same session (cookies)
    '''
    #capture session
    session = requests.Session()

    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    login_response = session.post(LOGIN_URL, data=payload)
    assert login_response.status_code == 200

    # Step 2: Load account overview page
    overview_response = session.get(OVERVIEW_URL)
    assert overview_response.status_code == 200

    #  Step 3: Extract numeric customerId from JS
    #     # services_proxy/bank/customers/12656/accounts
    match = re.search(
        r'\+\s*(\d+)\s*\+',
        overview_response.text
    )
    assert match is not None, "Customer ID not found in overview page"

    customer_id = match.group(1)

    return session, customer_id

def get_account_ids(session, customer_id):
    response = session.get(f"{BASE_URL}/services_proxy/bank/customers/{customer_id}/accounts")
    assert response.status_code == 200

    accounts = response.json()
    # print(accounts)
    # assert len(accounts) >= 2, "At least two accounts required for transfer"

    from_account = accounts[0]["id"]
    to_account = accounts[0]["id"]

    return from_account, to_account