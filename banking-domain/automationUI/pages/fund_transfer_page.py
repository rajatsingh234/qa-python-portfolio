from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FundTransferPage():
    def __init__(self, driver):
        self.driver = driver

    TRANSFER_FUNDS_LINK = (By.LINK_TEXT, "Transfer Funds")
    AMOUNT_INPUT = (By.ID, "amount")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    TO_ACCOUNT = (By.ID, "toAccountId")
    TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")
    SUCCESS_MESSAGE = (By.XPATH, "//h1[text()='Transfer Complete!']")

    def open_transfer_funds(self):
        return self.driver.find_element(*self.TRANSFER_FUNDS_LINK).click()

    def transfer_funds(self, amount):
        self.driver.find_element(*self.AMOUNT_INPUT).send_keys(amount)

        Select(self.driver.find_element(*self.FROM_ACCOUNT)).select_by_index(0)
        Select(self.driver.find_element(*self.TO_ACCOUNT)).select_by_index(0)

        self.driver.find_element(*self.TRANSFER_BUTTON).click()

    def is_transfer_successful(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).is_displayed()