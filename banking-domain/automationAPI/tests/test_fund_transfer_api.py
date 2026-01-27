from automationAPI.utils.api_client import get_authenticated_session, get_account_ids
BASE_URL = "https://parabank.parasoft.com/parabank"

def test_fund_transfer_api():
    session, customer_id = get_authenticated_session()
    from_account, to_account = get_account_ids(session, customer_id)

    payload = {
        "fromAccountId": from_account,
        "toAccountId": to_account,
        "amount": "1000"
    }

    response = session.post(f"{BASE_URL}/services_proxy/bank/transfer", data=payload)
    assert response.status_code == 200

    # ParaBank returns JSON confirmation
    result = response.text
    assert "Successfully transferred" in result