import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage

CONTACT_DETAILS_VALID_DATA = {
    "Street 1": "House 12, Road 5",
    "Street 2": "Block B",
    "City": "Dhaka",
    "State/Province": "Dhaka",
    "Zip/Postal Code": "1207",
    "Home": "+880-1711-111111",
    "Mobile": "+880-1811-222222",
    "Work": "+880-1911-333333",
    "Work Email": "work.user@example.com",
    "Other Email": "other.user@example.com",
}


def open_contact_details_page(driver):
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

    with allure.step("Open My Info Personal Details page"):
        my_info_page.open_my_info_page()
        my_info_page.wait_until_personal_details_page_is_loaded()

    with allure.step("Open Contact Details tab"):
        my_info_page.open_contact_details_tab()
        my_info_page.wait_until_contact_details_page_is_loaded()

    return my_info_page


@allure.feature("My Info")
@allure.story("Contact Details")
@allure.title("Verify Contact Details data can be updated and persisted")
def test_contact_details_data_can_be_updated_and_persisted(driver):
    my_info_page = open_contact_details_page(driver)

    print("\n========== CONTACT DETAILS UPDATE TEST ==========")

    with allure.step("Enter valid Contact Details data"):
        my_info_page.enter_contact_details_data(CONTACT_DETAILS_VALID_DATA)

    with allure.step("Save Contact Details form"):
        my_info_page.save_contact_details()

    with allure.step("Reopen Contact Details tab to verify persistence"):
        my_info_page.open_my_info_page()
        my_info_page.open_contact_details_tab()
        my_info_page.wait_until_contact_details_page_is_loaded()

    with allure.step("Verify saved Contact Details data"):
        my_info_page.verify_contact_details_data(CONTACT_DETAILS_VALID_DATA)

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Contact Details Data Updated and Persisted",
        attachment_type=allure.attachment_type.PNG,
    )

    print("Status: Contact Details data updated and persisted successfully")
    print("=================================================\n")
