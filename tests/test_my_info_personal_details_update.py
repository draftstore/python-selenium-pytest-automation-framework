import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


@allure.feature("My Info")
@allure.story("Personal Details Update")
@allure.title("Verify user can update and restore optional personal details")
def test_user_can_update_and_restore_optional_personal_details(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

    updated_other_id = "AUTO-OTHER-001"
    updated_license_number = "AUTO-LICENSE-001"

    with allure.step("Login to OrangeHRM with valid credentials"):
        login_page.load()
        login_page.login("Admin", "admin123")

    with allure.step("Verify dashboard is displayed after login"):
       assert dashboard_page.wait_until_dashboard_is_loaded(), (
           "Dashboard page was not displayed after login"
           )

    with allure.step("Open My Info page"):
        my_info_page.open_my_info_page()
        my_info_page.wait_until_personal_details_page_is_loaded()

    with allure.step("Verify Personal Details page is displayed"):
        assert my_info_page.is_personal_details_page_displayed(), (
            "Personal Details page was not displayed"
        )

    original_other_id = my_info_page.get_other_id_value()
    original_license_number = my_info_page.get_drivers_license_value()

    try:
        with allure.step("Update Other ID and Driver's License Number"):
            my_info_page.update_other_id(updated_other_id)
            my_info_page.update_drivers_license_number(updated_license_number)
            my_info_page.save_personal_details()

        with allure.step("Verify success message is displayed after update"):
            assert my_info_page.is_success_message_displayed(), (
                "Success message was not displayed after updating personal details"
            )

        with allure.step("Verify updated values are displayed correctly"):
            assert my_info_page.get_other_id_value() == updated_other_id, (
                "Updated Other ID value was not displayed correctly"
            )

            assert my_info_page.get_drivers_license_value() == updated_license_number, (
                "Updated Driver's License Number was not displayed correctly"
            )

    finally:
        with allure.step("Restore original Other ID and Driver's License Number"):
            my_info_page.update_other_id(original_other_id)
            my_info_page.update_drivers_license_number(original_license_number)
            my_info_page.save_personal_details()