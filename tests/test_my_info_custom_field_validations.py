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
@allure.story("Custom Fields Blood Type Dropdown")
@allure.title(
    "Verify each Blood Type option can be selected, saved, and restored to first option"
)
def test_blood_type_dropdown_all_options_and_restore_default(driver):
    my_info_page = open_personal_details_page(driver)

    with allure.step("Capture current displayed Blood Type value"):
        original_blood_type = my_info_page.get_blood_type_value()

        allure.attach(
            f"Original Displayed Blood Type Value: {original_blood_type}",
            name="Original Blood Type Value",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Get real selectable Blood Type options dynamically"):
        available_options = my_info_page.get_blood_type_options()

        assert available_options, "No Blood Type options were found"

        default_blood_type = available_options[0]

        testable_options = [option for option in available_options if option]

        allure.attach(
            f"Original Displayed Value: {original_blood_type}\n"
            f"Dynamic Default / First Real Option: {default_blood_type}\n\n"
            f"Testable Options:\n" + "\n".join(testable_options),
            name="Available Blood Type Options",
            attachment_type=allure.attachment_type.TEXT,
        )

        assert testable_options, "No selectable Blood Type options were found"

    try:
        for blood_type in testable_options:
            with allure.step(f"Select Blood Type option: {blood_type}"):
                my_info_page.update_blood_type(blood_type)

                actual_blood_type = my_info_page.get_blood_type_value()

                assert actual_blood_type == blood_type, (
                    f"Blood Type dropdown did not show selected value. "
                    f"Expected: {blood_type}, Actual: {actual_blood_type}"
                )

            with allure.step(f"Save selected Blood Type option: {blood_type}"):
                my_info_page.save_custom_fields()

                allure.attach(
                    f"Selected Blood Type: {blood_type}\n"
                    f"Displayed Value Before Save: {actual_blood_type}\n"
                    f"Save Button Clicked: Yes",
                    name=f"Blood Type Save Evidence - {blood_type}",
                    attachment_type=allure.attachment_type.TEXT,
                )

        with allure.step(
            "Restore Blood Type back to first real option dynamically and save"
        ):
            restored_default = my_info_page.restore_blood_type_default(
                default_blood_type
            )

            actual_default_value = my_info_page.get_blood_type_value()

            assert actual_default_value == restored_default, (
                f"Blood Type was not restored to first real option before save. "
                f"Expected: {restored_default}, Actual: {actual_default_value}"
            )

            my_info_page.save_custom_fields()

            allure.attach(
                f"Restored Blood Type To: {actual_default_value}\n"
                f"Expected First Real Option: {default_blood_type}\n"
                f"Save Button Clicked After Restore: Yes",
                name="Blood Type Restore and Save Evidence",
                attachment_type=allure.attachment_type.TEXT,
            )

    finally:
        with allure.step("Safety cleanup: ensure Blood Type remains first real option"):
            try:
                current_blood_type = my_info_page.get_blood_type_value()

                if current_blood_type != default_blood_type:
                    restored_default = my_info_page.restore_blood_type_default(
                        default_blood_type
                    )
                    my_info_page.save_custom_fields()
                else:
                    restored_default = default_blood_type

                final_blood_type = my_info_page.get_blood_type_value()

                assert final_blood_type == restored_default, (
                    f"Blood Type cleanup failed. "
                    f"Expected: {restored_default}, Actual: {final_blood_type}"
                )

                allure.attach(
                    f"Blood Type after cleanup: {final_blood_type}\n"
                    f"Expected First Real Option: {restored_default}",
                    name="Blood Type Cleanup Evidence",
                    attachment_type=allure.attachment_type.TEXT,
                )

            except Exception as cleanup_error:
                allure.attach(
                    str(cleanup_error),
                    name="Blood Type Cleanup Warning",
                    attachment_type=allure.attachment_type.TEXT,
                )
                raise


@allure.feature("My Info")
@allure.story("Custom Fields Test_Field Validation")
@allure.title("Verify maximum length validation for Test_Field")
def test_test_field_max_length_validation_and_restore_blank(driver):
    my_info_page = open_personal_details_page(driver)

    max_length_error_message = "Should not exceed 250 characters"
    long_test_field_value = "A" * 251

    with allure.step("Capture original Test_Field value"):
        original_test_field_value = my_info_page.get_test_field_value()

        allure.attach(
            f"Original Test_Field Value: {original_test_field_value}",
            name="Original Test_Field Value",
            attachment_type=allure.attachment_type.TEXT,
        )

    try:
        with allure.step("Enter more than 250 characters in Test_Field"):
            my_info_page.update_test_field(long_test_field_value)
            my_info_page.save_custom_fields()

        with allure.step("Verify maximum length validation message"):
            actual_error_message = my_info_page.get_test_field_error_message()

            assert actual_error_message == max_length_error_message, (
                f"Test_Field max length message mismatch. "
                f"Expected: '{max_length_error_message}', "
                f"Actual: '{actual_error_message}'"
            )

            allure.attach(
                f"Test_Field Length: {len(long_test_field_value)}\n"
                f"Expected Error: {max_length_error_message}\n"
                f"Actual Error: {actual_error_message}",
                name="Test_Field Maximum Length Validation Evidence",
                attachment_type=allure.attachment_type.TEXT,
            )

    finally:
        with allure.step("Restore Test_Field back to blank"):
            try:
                my_info_page.clear_test_field()

                final_test_field_value = my_info_page.get_test_field_value()

                assert final_test_field_value == "", (
                    f"Test_Field should be blank after cleanup. "
                    f"Actual: '{final_test_field_value}'"
                )

                allure.attach(
                    f"Final Test_Field Value: '{final_test_field_value}'",
                    name="Test_Field Cleanup Evidence",
                    attachment_type=allure.attachment_type.TEXT,
                )
            except Exception as cleanup_error:
                allure.attach(
                    str(cleanup_error),
                    name="Test_Field Cleanup Warning",
                    attachment_type=allure.attachment_type.TEXT,
                )
                raise
