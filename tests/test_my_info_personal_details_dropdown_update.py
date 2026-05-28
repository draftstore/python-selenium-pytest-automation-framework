import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


@allure.feature("My Info")
@allure.story("Personal Details Dropdown Update")
@allure.title("Verify user can update and restore nationality and marital status")
def test_user_can_update_and_restore_personal_details_dropdown_fields(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

    updated_nationality = "Bangladeshi"
    updated_marital_status = "Single"

    with allure.step("Login to OrangeHRM with valid credentials"):
        login_page.load()
        login_page.login("Admin", "admin123")

    with allure.step("Verify dashboard is displayed after login"):
        assert dashboard_page.wait_until_dashboard_is_loaded(), (
            "Dashboard page was not displayed after login"
        )

    with allure.step("Open My Info page"):
        my_info_page.open_my_info_page()

    with allure.step("Verify Personal Details page is displayed"):
        assert my_info_page.is_personal_details_page_displayed(), (
            "Personal Details page was not displayed"
        )

    original_nationality = my_info_page.get_nationality_value()
    original_marital_status = my_info_page.get_marital_status_value()

    allure.attach(
        f"Original Nationality: {original_nationality}\n"
        f"Original Marital Status: {original_marital_status}",
        name="Original Dropdown Values",
        attachment_type=allure.attachment_type.TEXT
    )

    try:
        with allure.step("Update Nationality and Marital Status"):
            my_info_page.update_nationality(updated_nationality)
            my_info_page.update_marital_status(updated_marital_status)
            my_info_page.save_personal_details()

        with allure.step("Verify success message is displayed after update"):
            assert my_info_page.is_success_message_displayed(), (
                "Success message was not displayed after updating dropdown fields"
            )

        with allure.step("Verify updated dropdown values are displayed correctly"):
            assert my_info_page.get_nationality_value() == updated_nationality, (
                "Updated Nationality value was not displayed correctly"
            )

            assert my_info_page.get_marital_status_value() == updated_marital_status, (
                "Updated Marital Status value was not displayed correctly"
            )

        allure.attach(
                f"Updated Nationality: {my_info_page.get_nationality_value()}\n"
                f"Updated Marital Status: {my_info_page.get_marital_status_value()}",
                name="Updated Dropdown Values",
                attachment_type=allure.attachment_type.TEXT
            )

    finally:
        with allure.step("Restore original Nationality and Marital Status if original values are selectable"):
            if original_nationality and original_nationality != "-- Select --":
                my_info_page.update_nationality(original_nationality)

            if original_marital_status and original_marital_status != "-- Select --":
                my_info_page.update_marital_status(original_marital_status)

            my_info_page.save_personal_details()