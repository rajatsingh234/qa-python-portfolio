from automationUI.pages.login_page import LoginPage
from automationUI.pages.account_overview_page import AccountOverViewPage

def test_login_negative(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("invalidUser", "wrongPassword")

    assert "error" in login_page.get_error_message()