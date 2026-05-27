from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class LoginPage(BasePage):
    """
    Page Object Model class for OrangeHRM Login Page.
    """

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")

    def load(self):
        self.open_url(ConfigReader.get_base_url())

    def login(self, username: str, password: str):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_page_displayed(self):
        return self.is_element_visible(self.LOGIN_BUTTON)