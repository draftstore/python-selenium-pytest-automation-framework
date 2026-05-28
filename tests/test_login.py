from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_user_can_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.load()
    login_page.login("Admin", "admin123")

    assert dashboard_page.wait_until_dashboard_is_loaded(), (
        "Dashboard page was not displayed after valid login"
    )