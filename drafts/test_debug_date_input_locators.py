from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


def test_debug_date_input_locators(driver):
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

    date_inputs = driver.find_elements(By.XPATH, "//input[@placeholder='yyyy-dd-mm']")

    print(f"\nTotal date inputs found: {len(date_inputs)}")

    for index, element in enumerate(date_inputs, start=1):
        value = element.get_attribute("value")
        outer_html = element.get_attribute("outerHTML")
        location = element.location
        size = element.size

        driver.execute_script("arguments[0].style.border='4px solid red';", element)

        print("\n-----------------------------")
        print(f"Date Input Index: {index}")
        print(f"Value: {value}")
        print(f"Location: {location}")
        print(f"Size: {size}")
        print(f"OuterHTML: {outer_html}")
