from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


def test_debug_blood_type_dropdown_options(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

    login_page.load()
    login_page.login("Admin", "admin123")

    assert (
        dashboard_page.wait_until_dashboard_is_loaded()
    ), "Dashboard page was not displayed after login"

    my_info_page.open_my_info_page()
    my_info_page.wait_until_personal_details_page_is_loaded()

    displayed_value = my_info_page.get_blood_type_value()
    print(f"\nDisplayed Blood Type value before opening dropdown: '{displayed_value}'")

    my_info_page.click(my_info_page.BLOOD_TYPE_DROPDOWN)

    option_elements = driver.find_elements(By.XPATH, "//div[@role='option']//span")

    print(f"Total Blood Type dropdown options found: {len(option_elements)}")

    for index, option in enumerate(option_elements, start=1):
        print(f"Option {index}: '{option.text.strip()}'")
