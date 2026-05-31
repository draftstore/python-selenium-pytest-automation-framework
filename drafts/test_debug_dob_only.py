from datetime import date
import time

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


def test_debug_dob_only(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

    test_dob = date(date.today().year - 25, 5, 15).strftime("%Y-%d-%m")

    login_page.load()
    login_page.login("Admin", "admin123")

    assert (
        dashboard_page.wait_until_dashboard_is_loaded()
    ), "Dashboard page was not displayed after login"

    my_info_page.open_my_info_page()
    my_info_page.wait_until_personal_details_page_is_loaded()

    print(f"\nDOB before update: '{my_info_page.get_date_of_birth_value()}'")

    my_info_page.update_date_of_birth(test_dob)

    time.sleep(3)

    actual_dob = my_info_page.get_date_of_birth_value()

    print(f"DOB expected: '{test_dob}'")
    print(f"DOB actual: '{actual_dob}'")

    assert (
        actual_dob == test_dob
    ), f"DOB was not entered correctly. Expected: '{test_dob}', Actual: '{actual_dob}'"

    my_info_page.save_personal_details()

    assert (
        my_info_page.is_success_message_displayed()
    ), "Success message was not displayed after saving DOB"

    print("DOB was selected from datepicker and save success message was displayed.")
