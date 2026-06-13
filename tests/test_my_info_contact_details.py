import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage

CONTACT_DETAILS_INPUT_FIELDS = [
    "Street 1",
    "Street 2",
    "City",
    "State/Province",
    "Zip/Postal Code",
    "Home",
    "Mobile",
    "Work",
    "Work Email",
    "Other Email",
]

CONTACT_DETAILS_SECTIONS = [
    "Address",
    "Telephone",
    "Email",
]


@allure.feature("My Info")
@allure.story("Contact Details")
@allure.title("Verify Contact Details tab structure and fields are displayed")
def test_contact_details_tab_structure_and_fields_are_displayed(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)
    visible_sections = []
    visible_fields = []

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

    with allure.step("Verify Contact Details header is displayed"):
        assert (
            my_info_page.is_contact_details_header_displayed()
        ), "Contact Details header was not displayed"

        my_info_page.highlight_contact_details_header()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Contact Details Header Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Verify Contact Details sections are displayed"):
        for section_name in CONTACT_DETAILS_SECTIONS:
            assert my_info_page.is_contact_details_section_displayed(
                section_name
            ), f"Contact Details section was not displayed: {section_name}"
            visible_sections.append(section_name)
            print(f"Visible Section: {section_name}")

    with allure.step("Verify Contact Details input fields are displayed"):
        for field_label in CONTACT_DETAILS_INPUT_FIELDS:
            assert my_info_page.is_contact_details_input_displayed(
                field_label
            ), f"Contact Details input field was not displayed: {field_label}"
            visible_fields.append(field_label)
            print(f"Visible Field: {field_label}")
            my_info_page.highlight_contact_details_input(field_label)

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Contact Details Input Fields Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Verify Country dropdown is displayed"):
        assert (
            my_info_page.is_contact_details_country_dropdown_displayed()
        ), "Country dropdown was not displayed"

        my_info_page.highlight_contact_details_country_dropdown()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Country Dropdown Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Verify Contact Details Save button is displayed"):
        assert (
            my_info_page.is_contact_details_save_button_displayed()
        ), "Contact Details Save button was not displayed"

        my_info_page.highlight_contact_details_save_button()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Contact Details Save Button Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    print("\n========== CONTACT DETAILS VISIBILITY SUMMARY ==========")
    print(f"Total Visible Sections: {len(visible_sections)}")
    print(f"Sections: {', '.join(visible_sections)}")
    print(f"Total Visible Input Fields: {len(visible_fields)}")
    print(f"Fields: {', '.join(visible_fields)}")
    print("Dropdown: Country")
    print("Button: Save")
    print("Contact Details structure test completed successfully")
    print("=======================================================\n")
