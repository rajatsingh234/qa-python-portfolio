from selenium.webdriver.common.by import By
from automationUI.config.config import BASE_URL

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    #locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error")

    #Actions
    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
