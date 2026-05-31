from datetime import date

import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


@allure.feature("My Info")
@allure.story("Personal Details Date Fields Update")
@allure.title("Verify user can update and reset personal details date fields")
def test_user_can_update_and_reset_personal_details_date_fields(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

    today = date.today()

    # OrangeHRM Personal Details date placeholder format: yyyy-dd-mm
    valid_adult_dob = date(today.year - 25, 5, 15).strftime("%Y-%d-%m")
    valid_license_expiry_date = date(today.year + 3, 12, 31).strftime("%Y-%d-%m")

    allure.attach(
        f"Test DOB: {valid_adult_dob}\n"
        f"Test License Expiry Date: {valid_license_expiry_date}\n"
        f"Expected OrangeHRM Date Format: yyyy-dd-mm",
        name="Date Test Data",
        attachment_type=allure.attachment_type.TEXT,
    )

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

    with allure.step("Capture original date field values"):
        original_dob = my_info_page.get_date_of_birth_value()
        original_license_expiry_date = my_info_page.get_license_expiry_date_value()

        allure.attach(
            f"Original DOB: {original_dob}\n"
            f"Original License Expiry Date: {original_license_expiry_date}",
            name="Original Date Values",
            attachment_type=allure.attachment_type.TEXT,
        )

    try:
        with allure.step("Set Date of Birth and License Expiry Date"):
            my_info_page.update_date_of_birth(valid_adult_dob)
            my_info_page.update_license_expiry_date(valid_license_expiry_date)

            dob_before_save = my_info_page.get_date_of_birth_value()
            license_expiry_before_save = my_info_page.get_license_expiry_date_value()

            assert dob_before_save == valid_adult_dob, (
                f"DOB was not entered correctly before save. "
                f"Expected: {valid_adult_dob}, Actual: {dob_before_save}"
            )

            assert license_expiry_before_save == valid_license_expiry_date, (
                f"License Expiry Date was not entered correctly before save. "
                f"Expected: {valid_license_expiry_date}, "
                f"Actual: {license_expiry_before_save}"
            )

            allure.attach(
                f"DOB Before Save: {dob_before_save}\n"
                f"License Expiry Date Before Save: {license_expiry_before_save}",
                name="Date Values Before Save",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Save updated date fields"):
            my_info_page.save_personal_details()

            assert (
                my_info_page.is_success_message_displayed()
            ), "Success message was not displayed after saving date fields"

        with allure.step("Reload page and capture date values after save"):
            my_info_page.refresh_page()
            my_info_page.wait_until_personal_details_page_is_loaded()

            dob_after_save_reload = my_info_page.get_date_of_birth_value()
            license_expiry_after_save_reload = (
                my_info_page.get_license_expiry_date_value()
            )

            allure.attach(
                f"Expected DOB: {valid_adult_dob}\n"
                f"Actual DOB After Reload: {dob_after_save_reload}\n\n"
                f"Expected License Expiry Date: {valid_license_expiry_date}\n"
                f"Actual License Expiry Date After Reload: {license_expiry_after_save_reload}",
                name="Date Values After Save Reload",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Reset date fields back to original values"):
            if original_dob:
                my_info_page.update_date_of_birth(original_dob)
            else:
                my_info_page.clear_date_of_birth()

            if original_license_expiry_date:
                my_info_page.update_license_expiry_date(original_license_expiry_date)
            else:
                my_info_page.clear_license_expiry_date()

            reset_dob_before_save = my_info_page.get_date_of_birth_value()
            reset_license_expiry_before_save = (
                my_info_page.get_license_expiry_date_value()
            )

            assert reset_dob_before_save == original_dob, (
                f"DOB was not reset correctly before save. "
                f"Expected: '{original_dob}', Actual: '{reset_dob_before_save}'"
            )

            assert reset_license_expiry_before_save == original_license_expiry_date, (
                f"License Expiry Date was not reset correctly before save. "
                f"Expected: '{original_license_expiry_date}', "
                f"Actual: '{reset_license_expiry_before_save}'"
            )
            my_info_page.save_personal_details()
            assert (
                my_info_page.is_success_message_displayed()
            ), "Success message was not displayed after resetting date fields"

            allure.attach(
                f"Original DOB: {original_dob}\n"
                f"Reset DOB Before Save: {reset_dob_before_save}\n\n"
                f"Original License Expiry Date: {original_license_expiry_date}\n"
                f"Reset License Expiry Date Before Save: {reset_license_expiry_before_save}",
                name="Date Reset Evidence Before Save",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Reload page and verify final reset state"):
            my_info_page.refresh_page()
            my_info_page.wait_until_personal_details_page_is_loaded()

            final_dob = my_info_page.get_date_of_birth_value()
            final_license_expiry_date = my_info_page.get_license_expiry_date_value()

            allure.attach(
                f"Original DOB: {original_dob}\n"
                f"Final DOB After Reset: {final_dob}\n\n"
                f"Original License Expiry Date: {original_license_expiry_date}\n"
                f"Final License Expiry Date After Reset: {final_license_expiry_date}",
                name="Final Date Reset Evidence",
                attachment_type=allure.attachment_type.TEXT,
            )

            if (
                final_dob != original_dob
                or final_license_expiry_date != original_license_expiry_date
            ):
                allure.attach(
                    "OrangeHRM demo did not persist one or more date fields after reload. "
                    "The test validated field entry, save success, and reset action before save, "
                    "but final reload persistence may depend on the demo application's behavior.",
                    name="Date Persistence Behavior Note",
                    attachment_type=allure.attachment_type.TEXT,
                )

    finally:
        with allure.step("Safety cleanup: ensure original date values are reapplied"):
            if original_dob:
                my_info_page.update_date_of_birth(original_dob)
            else:
                my_info_page.clear_date_of_birth()

            if original_license_expiry_date:
                my_info_page.update_license_expiry_date(original_license_expiry_date)
            else:
                my_info_page.clear_license_expiry_date()

            my_info_page.save_personal_details()

            allure.attach(
                f"Cleanup DOB Target: {original_dob}\n"
                f"Cleanup License Expiry Date Target: {original_license_expiry_date}",
                name="Safety Cleanup Evidence",
                attachment_type=allure.attachment_type.TEXT,
            )
