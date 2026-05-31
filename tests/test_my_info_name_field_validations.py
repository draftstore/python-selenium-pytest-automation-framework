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
@allure.story("Personal Details Name Field Validation")
@allure.title("Verify required validation for First Name and Last Name")
def test_required_validation_for_first_and_last_name(driver):
    my_info_page = open_personal_details_page(driver)

    required_error_message = "Required"

    with allure.step("Capture original name field values"):
        original_first_name = my_info_page.get_first_name_value()
        original_middle_name = my_info_page.get_middle_name_value()
        original_last_name = my_info_page.get_last_name_value()

        allure.attach(
            f"Original First Name: {original_first_name}\n"
            f"Original Middle Name: {original_middle_name}\n"
            f"Original Last Name: {original_last_name}",
            name="Original Name Field Values",
            attachment_type=allure.attachment_type.TEXT,
        )

    try:
        with allure.step("Clear First Name, Middle Name, and Last Name"):
            my_info_page.update_first_name("")
            my_info_page.update_middle_name("")
            my_info_page.update_last_name("")
            my_info_page.save_personal_details()

        with allure.step("Verify required validation messages"):
            first_name_error = my_info_page.get_first_name_error_message()
            last_name_error = my_info_page.get_last_name_error_message()
            middle_name_error_displayed = my_info_page.is_middle_name_error_displayed()

            assert first_name_error == required_error_message, (
                f"First Name required message mismatch. "
                f"Expected: '{required_error_message}', Actual: '{first_name_error}'"
            )

            assert last_name_error == required_error_message, (
                f"Last Name required message mismatch. "
                f"Expected: '{required_error_message}', Actual: '{last_name_error}'"
            )

            assert (
                not middle_name_error_displayed
            ), "Middle Name should not show required validation because it is optional"

            allure.attach(
                f"First Name Error: {first_name_error}\n"
                f"Middle Name Required Error Displayed: {middle_name_error_displayed}\n"
                f"Last Name Error: {last_name_error}",
                name="Required Validation Evidence",
                attachment_type=allure.attachment_type.TEXT,
            )

    finally:
        with allure.step("Restore original name field values"):
            my_info_page.restore_name_fields(
                original_first_name or "Admin",
                original_middle_name or "",
                original_last_name or "User",
            )

            assert (
                my_info_page.is_success_message_displayed()
            ), "Success message was not displayed after restoring original name values"


@allure.feature("My Info")
@allure.story("Personal Details Name Field Validation")
@allure.title("Verify maximum length validation for First, Middle, and Last Name")
def test_max_length_validation_for_name_fields(driver):
    my_info_page = open_personal_details_page(driver)

    max_length_error_message = "Should not exceed 30 characters"

    long_first_name = "A" * 31
    long_middle_name = "B" * 31
    long_last_name = "C" * 31

    with allure.step("Capture original name field values"):
        original_first_name = my_info_page.get_first_name_value()
        original_middle_name = my_info_page.get_middle_name_value()
        original_last_name = my_info_page.get_last_name_value()

        allure.attach(
            f"Original First Name: {original_first_name}\n"
            f"Original Middle Name: {original_middle_name}\n"
            f"Original Last Name: {original_last_name}",
            name="Original Name Field Values",
            attachment_type=allure.attachment_type.TEXT,
        )

    try:
        with allure.step("Enter more than 30 characters in name fields"):
            my_info_page.update_first_name(long_first_name)
            my_info_page.update_middle_name(long_middle_name)
            my_info_page.update_last_name(long_last_name)
            my_info_page.save_personal_details()

        with allure.step("Verify maximum length validation messages"):
            first_name_error = my_info_page.get_first_name_error_message()
            middle_name_error = my_info_page.get_middle_name_error_message()
            last_name_error = my_info_page.get_last_name_error_message()

            assert first_name_error == max_length_error_message, (
                f"First Name max length message mismatch. "
                f"Expected: '{max_length_error_message}', Actual: '{first_name_error}'"
            )

            assert middle_name_error == max_length_error_message, (
                f"Middle Name max length message mismatch. "
                f"Expected: '{max_length_error_message}', Actual: '{middle_name_error}'"
            )

            assert last_name_error == max_length_error_message, (
                f"Last Name max length message mismatch. "
                f"Expected: '{max_length_error_message}', Actual: '{last_name_error}'"
            )

            allure.attach(
                f"First Name Length: {len(long_first_name)} | Error: {first_name_error}\n"
                f"Middle Name Length: {len(long_middle_name)} | Error: {middle_name_error}\n"
                f"Last Name Length: {len(long_last_name)} | Error: {last_name_error}",
                name="Maximum Length Validation Evidence",
                attachment_type=allure.attachment_type.TEXT,
            )

    finally:
        with allure.step("Restore original name field values"):
            my_info_page.restore_name_fields(
                original_first_name or "Admin",
                original_middle_name or "",
                original_last_name or "User",
            )

            assert (
                my_info_page.is_success_message_displayed()
            ), "Success message was not displayed after restoring original name values"
