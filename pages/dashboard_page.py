from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    """
    Page Object Model class for OrangeHRM Dashboard Page.
    """

    DASHBOARD_HEADER = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-name")
    LOGOUT_LINK = (By.XPATH, "//a[normalize-space()='Logout']")

    def wait_until_dashboard_is_loaded(self):
        self.wait_for_url_contains("dashboard")
        return self.is_dashboard_displayed()

    def is_dashboard_displayed(self):
        return self.is_element_visible(self.DASHBOARD_HEADER)

    def get_dashboard_header_text(self):
        return self.get_text(self.DASHBOARD_HEADER)

    def logout(self):
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_LINK)