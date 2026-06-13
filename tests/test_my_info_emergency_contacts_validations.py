import allure
import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


def open_emergency_contacts_page(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

    with allure.step("Login to OrangeHRM"):
        login_page.load()
        login_page.login("Admin", "admin123")

    with allure.step("Verify dashboard is displayed"):
        assert (
            dashboard_page.wait_until_dashboard_is_loaded()
        ), "Dashboard page was not displayed after login"

    with allure.step("Open My Info page"):
        my_info_page.open_my_info_page()
        my_info_page.wait_until_personal_details_page_is_loaded()

    with allure.step("Open Emergency Contacts tab"):
        my_info_page.open_emergency_contacts_tab()
        my_info_page.wait_until_emergency_contacts_page_is_loaded()

    return my_info_page


@allure.feature("My Info")
@allure.story("Emergency Contacts")
@allure.title("Verify Emergency Contacts Add form is displayed")
def test_emergency_contacts_add_form_is_displayed(driver):
    my_info_page = open_emergency_contacts_page(driver)

    with allure.step("Click Emergency Contacts Add button"):
        my_info_page.click_emergency_contacts_add_button()

    with allure.step("Verify Save Emergency Contact form is displayed"):
        assert my_info_page.wait_until_emergency_contact_form_is_displayed()

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Emergency Contact Add Form Displayed",
        attachment_type=allure.attachment_type.PNG,
    )


@allure.feature("My Info")
@allure.story("Emergency Contacts")
@allure.title("Verify Emergency Contact required validation messages")
def test_emergency_contact_required_validation_messages_are_displayed(driver):
    my_info_page = open_emergency_contacts_page(driver)

    required_validation_data = {
        "Name": "Required",
        "Relationship": "Required",
        "Home Telephone": "At least one phone number is required",
    }

    with allure.step("Click Emergency Contacts Add button"):
        my_info_page.click_emergency_contacts_add_button()
        my_info_page.wait_until_emergency_contact_form_is_displayed()

    with allure.step("Save Emergency Contact form without required data"):
        my_info_page.save_emergency_contact()

    with allure.step("Verify all required validation messages"):
        for field_label, expected_error_message in required_validation_data.items():
            my_info_page.wait_until_emergency_contact_field_error_is_displayed(
                field_label,
                expected_error_message,
            )

            actual_error_message = (
                my_info_page.get_emergency_contact_field_error_message(field_label)
            )

            assert expected_error_message in actual_error_message, (
                f"Expected required validation message was not displayed "
                f"for field: {field_label}. "
                f"Expected: '{expected_error_message}', "
                f"Actual: '{actual_error_message}'"
            )

            my_info_page.highlight_emergency_contact_input(field_label)
            my_info_page.highlight_emergency_contact_field_error(field_label)

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Emergency Contact Required Validations Highlighted",
        attachment_type=allure.attachment_type.PNG,
    )
