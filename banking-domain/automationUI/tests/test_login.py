from automationUI.pages.login_page import LoginPage
from automationUI.pages.account_overview_page import AccountOverViewPage

def test_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    account_page = AccountOverViewPage(driver)

    login_page.open()
    login_page.login("testbankuser03", "Test@123")

    assert account_page.is_account_overview_page_displayed()
