import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage

EMERGENCY_CONTACT_VALID_DATA = {
    "Name": "Rahim Uddin",
    "Relationship": "Brother",
    "Home Telephone": "+880-2-123456",
    "Mobile": "+880-1711-222333",
    "Work Telephone": "+880-2-987654",
}


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
@allure.title("Verify Emergency Contact data can be added and displayed in table")
def test_emergency_contact_data_can_be_added_and_displayed_in_table(driver):
    my_info_page = open_emergency_contacts_page(driver)

    print("\n========== EMERGENCY CONTACT DATA INSERT TEST ==========")

    with allure.step("Click Emergency Contacts Add button"):
        my_info_page.click_emergency_contacts_add_button()
        my_info_page.wait_until_emergency_contact_form_is_displayed()

    with allure.step("Enter valid Emergency Contact data"):
        my_info_page.enter_emergency_contact_data(EMERGENCY_CONTACT_VALID_DATA)

    with allure.step("Verify entered Emergency Contact data before save"):
        my_info_page.verify_emergency_contact_data_in_form(EMERGENCY_CONTACT_VALID_DATA)

    with allure.step("Save Emergency Contact form"):
        my_info_page.save_emergency_contact()

    with allure.step("Verify Emergency Contact is displayed in table"):
        my_info_page.verify_emergency_contact_saved_in_table(
            EMERGENCY_CONTACT_VALID_DATA
        )

    with allure.step("Highlight saved Emergency Contact table row"):
        my_info_page.highlight_emergency_contact_table_row(
            EMERGENCY_CONTACT_VALID_DATA["Name"]
        )

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Emergency Contact Data Inserted and Displayed",
        attachment_type=allure.attachment_type.PNG,
    )

    print("Status: Emergency Contact data added and displayed successfully")
    print("========================================================\n")
