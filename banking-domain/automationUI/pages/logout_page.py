from selenium.webdriver.common.by import By

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    LOGOUT_LINK = (By.LINK_TEXT, "Log Out")

    def logout(self):
        return self.driver.find_element(*self.LOGOUT_LINK).click()