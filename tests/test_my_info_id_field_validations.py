import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


def open_personal_details_page(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

    with allure.step("Login to OrangeHRM with valid credentials"):
        login_page.load()
        login_page.login("Admin", "admin123")

    with allure.step("Verify dashboard is displayed after login"):
        assert (
            dashboard_page.wait_until_dashboard_is_loaded()
        ), "Dashboard page was not displayed after login"

    with allure.step("Open My Info Personal Details page"):
        my_info_page.open_my_info_page()
        my_info_page.wait_until_personal_details_page_is_loaded()

    return my_info_page


@allure.feature("My Info")
@allure.story("Personal Details ID Field Validation")
@allure.title(
    "Verify maximum length validation for Employee Id, Other Id, and Driver's License Number"
)
def test_max_length_validation_for_id_fields(driver):
    my_info_page = open_personal_details_page(driver)

    long_employee_id = "1" * 11
    long_other_id = "A" * 31
    long_drivers_license_number = "L" * 31

    employee_id_error_message = "Should not exceed 10 characters"
    other_id_error_message = "Should not exceed 30 characters"
    drivers_license_error_message = "Should not exceed 30 characters"

    with allure.step("Capture original ID field values"):
        original_employee_id = my_info_page.get_employee_id_value()
        original_other_id = my_info_page.get_other_id_value()
        original_drivers_license_number = my_info_page.get_drivers_license_value()

        allure.attach(
            f"Original Employee Id: {original_employee_id}\n"
            f"Original Other Id: {original_other_id}\n"
            f"Original Driver's License Number: {original_drivers_license_number}",
            name="Original ID Field Values",
            attachment_type=allure.attachment_type.TEXT,
        )

    try:
        with allure.step("Enter values exceeding maximum allowed length"):
            my_info_page.update_employee_id(long_employee_id)
            my_info_page.update_other_id(long_other_id)
            my_info_page.update_drivers_license_number(long_drivers_license_number)
            my_info_page.save_personal_details()

        with allure.step("Verify maximum length validation messages"):
            actual_employee_id_error = my_info_page.get_employee_id_error_message()
            actual_other_id_error = my_info_page.get_other_id_error_message()
            actual_drivers_license_error = (
                my_info_page.get_drivers_license_error_message()
            )

            assert actual_employee_id_error == employee_id_error_message, (
                f"Employee Id max length message mismatch. "
                f"Expected: '{employee_id_error_message}', "
                f"Actual: '{actual_employee_id_error}'"
            )

            assert actual_other_id_error == other_id_error_message, (
                f"Other Id max length message mismatch. "
                f"Expected: '{other_id_error_message}', "
                f"Actual: '{actual_other_id_error}'"
            )

            assert actual_drivers_license_error == drivers_license_error_message, (
                f"Driver's License Number max length message mismatch. "
                f"Expected: '{drivers_license_error_message}', "
                f"Actual: '{actual_drivers_license_error}'"
            )

            allure.attach(
                f"Employee Id Length: {len(long_employee_id)} | "
                f"Error: {actual_employee_id_error}\n"
                f"Other Id Length: {len(long_other_id)} | "
                f"Error: {actual_other_id_error}\n"
                f"Driver's License Number Length: {len(long_drivers_license_number)} | "
                f"Error: {actual_drivers_license_error}",
                name="ID Field Maximum Length Validation Evidence",
                attachment_type=allure.attachment_type.TEXT,
            )

    finally:
        with allure.step("Restore original ID field values"):
            my_info_page.restore_id_fields(
                original_employee_id or "",
                original_other_id or "",
                original_drivers_license_number or "",
            )

            assert (
                my_info_page.is_success_message_displayed()
            ), "Success message was not displayed after restoring original ID field values"
