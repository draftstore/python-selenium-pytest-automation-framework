from datetime import date
import time

import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


@allure.feature("My Info")
@allure.story("Personal Details Date Field UI Interaction")
@allure.title(
    "Verify DOB and License Expiry Date can be selected, saved, cleared, and reset"
)
def test_date_fields_can_be_selected_saved_cleared_and_reset(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

    today = date.today()

    test_dob = date(today.year - 25, 5, 15).strftime("%Y-%d-%m")
    test_license_expiry = date(today.year, 5, 15).strftime("%Y-%d-%m")

    with allure.step("Login to OrangeHRM"):
        login_page.load()
        login_page.login("Admin", "admin123")

    with allure.step("Verify dashboard is displayed"):
        assert (
            dashboard_page.wait_until_dashboard_is_loaded()
        ), "Dashboard page was not displayed after login"

    with allure.step("Open My Info Personal Details page"):
        my_info_page.open_my_info_page()
        my_info_page.wait_until_personal_details_page_is_loaded()

    with allure.step("Capture initial date values"):
        initial_dob = my_info_page.get_date_of_birth_value()
        initial_license_expiry = my_info_page.get_license_expiry_date_value()

        allure.attach(
            f"Initial DOB: '{initial_dob}'\n"
            f"Initial License Expiry Date: '{initial_license_expiry}'",
            name="Initial Date Field Values",
            attachment_type=allure.attachment_type.TEXT,
        )

    try:
        with allure.step("Ensure date fields are blank before test"):
            if initial_dob:
                my_info_page.clear_date_of_birth()

            if initial_license_expiry:
                my_info_page.clear_license_expiry_date()

            cleared_initial_dob = my_info_page.get_date_of_birth_value()
            cleared_initial_license_expiry = (
                my_info_page.get_license_expiry_date_value()
            )

            assert cleared_initial_dob == "", (
                f"DOB should be blank before test. " f"Actual: '{cleared_initial_dob}'"
            )

            assert cleared_initial_license_expiry == "", (
                f"License Expiry Date should be blank before test. "
                f"Actual: '{cleared_initial_license_expiry}'"
            )

            my_info_page.save_personal_details()

            assert (
                my_info_page.is_success_message_displayed()
            ), "Success message was not displayed after clearing initial date values"

        with allure.step("Select DOB and License Expiry Date from datepicker"):
            my_info_page.update_date_of_birth(test_dob)
            my_info_page.update_license_expiry_date(test_license_expiry)

            time.sleep(3)

            actual_dob = my_info_page.get_date_of_birth_value()
            actual_license_expiry = my_info_page.get_license_expiry_date_value()

            assert actual_dob == test_dob, (
                f"DOB was not selected correctly. "
                f"Expected: '{test_dob}', Actual: '{actual_dob}'"
            )

            assert actual_license_expiry == test_license_expiry, (
                f"License Expiry Date was not selected correctly. "
                f"Expected: '{test_license_expiry}', Actual: '{actual_license_expiry}'"
            )

            allure.attach(
                f"DOB After Selection: '{actual_dob}'\n"
                f"License Expiry Date After Selection: '{actual_license_expiry}'",
                name="Date Values After Selection",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Save selected date values"):
            my_info_page.save_personal_details()

            assert (
                my_info_page.is_success_message_displayed()
            ), "Success message was not displayed after saving selected date values"

        with allure.step("Clear DOB and License Expiry Date back to blank"):
            my_info_page.clear_date_of_birth()
            my_info_page.clear_license_expiry_date()

            time.sleep(3)

            cleared_dob = my_info_page.get_date_of_birth_value()
            cleared_license_expiry = my_info_page.get_license_expiry_date_value()

            assert (
                cleared_dob == ""
            ), f"DOB was not cleared correctly. Actual: '{cleared_dob}'"

            assert cleared_license_expiry == "", (
                f"License Expiry Date was not cleared correctly. "
                f"Actual: '{cleared_license_expiry}'"
            )

            allure.attach(
                f"DOB After Clear: '{cleared_dob}'\n"
                f"License Expiry Date After Clear: '{cleared_license_expiry}'",
                name="Date Values After Clear",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Save blank reset values"):
            my_info_page.save_personal_details()

            assert (
                my_info_page.is_success_message_displayed()
            ), "Success message was not displayed after saving blank reset values"

    finally:
        with allure.step("Safety cleanup: keep date fields blank"):
            try:
                my_info_page.clear_date_of_birth()
                my_info_page.clear_license_expiry_date()
                my_info_page.save_personal_details()
            except Exception as cleanup_error:
                allure.attach(
                    str(cleanup_error),
                    name="Date Field Cleanup Warning",
                    attachment_type=allure.attachment_type.TEXT,
                )
