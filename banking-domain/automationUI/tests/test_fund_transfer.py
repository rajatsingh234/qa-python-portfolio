import pytest
from automationUI.pages.login_page import LoginPage
from automationUI.pages.fund_transfer_page import FundTransferPage

@pytest.mark.smoke
def test_fund_transfer(setup):

    driver = setup
    driver.implicitly_wait(5)

    login_page = LoginPage(driver)
    fund_transfer_page = FundTransferPage(driver)

    login_page.open()
    login_page.login("testbankuser03", "Test@123")

    fund_transfer_page.open_transfer_funds()
    fund_transfer_page.transfer_funds("100")

    assert fund_transfer_page.is_transfer_successful()
