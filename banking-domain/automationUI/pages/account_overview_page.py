from selenium.webdriver.common.by import By

class AccountOverViewPage:
    def __init__(self, driver):
        self.driver = driver

    ACCOUNT_OVERVIEW_HEADER = (By.XPATH, "//h1[contains(text(),'Accounts Overview')]")

    def is_account_overview_page_displayed(self):
        return self.driver.find_element(*self.ACCOUNT_OVERVIEW_HEADER).is_displayed()