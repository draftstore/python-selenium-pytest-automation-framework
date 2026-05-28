from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


def test_personal_details_page_loads_with_required_fields(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

    login_page.load()
    login_page.login("Admin", "admin123")
    
    assert dashboard_page.wait_until_dashboard_is_loaded(), (
    "Dashboard page was not displayed after login"
    )

    my_info_page.open_my_info_page()
    my_info_page.wait_until_personal_details_page_is_loaded()

    assert my_info_page.is_personal_details_page_displayed(), (
        "Personal Details page was not displayed"
    )

    assert my_info_page.are_name_fields_visible(), (
        "First Name, Middle Name, or Last Name field is not visible"
    )

    assert my_info_page.are_id_fields_visible(), (
        "Employee ID, Other ID, Driver's License, or License Expiry Date field is not visible"
    )

    assert my_info_page.are_personal_information_fields_visible(), (
        "Nationality, Marital Status, Date of Birth, or Gender field is not visible"
    )

    assert my_info_page.is_save_button_visible(), (
        "Personal Details Save button is not visible"
    )