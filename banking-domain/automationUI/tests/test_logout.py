from automationUI.pages.login_page import LoginPage
from automationUI.pages.logout_page import LogoutPage

def test_logout(setup):
    driver = setup
    login_page = LoginPage(driver)
    logout_page = LogoutPage(driver)

    login_page.open()
    login_page.login("testbankuser03", "Test@123")

    logout_page.logout()

    assert "Customer Login" in driver.page_source
