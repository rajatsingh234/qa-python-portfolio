from automationAPI.utils.api_client import get_authenticated_session

ACCOUNTS_URL = "https://parabank.parasoft.com/parabank/services_proxy/bank/accounts"
BASE_URL = "https://parabank.parasoft.com/parabank"

def test_get_account_api():
    session, customer_id = get_authenticated_session()

    response = session.get(
        f"{BASE_URL}/services_proxy/bank/customers/{customer_id}/accounts"
    )
    print(response.json())
    assert response.status_code == 200

    accounts = response.json()

    # Validate response structure
    assert isinstance(accounts, list)
    assert len(accounts) > 0

    # Validate account fields
    account = accounts[0]
    assert "id" in account
    assert "customerId" in account
    assert "balance" in account