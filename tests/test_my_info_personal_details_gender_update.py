import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


@allure.feature("My Info")
@allure.story("Personal Details Gender Update")
@allure.title("Verify user can update and restore gender selection")
def test_user_can_update_and_restore_gender_selection(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

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

    original_gender = my_info_page.get_selected_gender()

    updated_gender = "Female" if original_gender == "Male" else "Male"

    allure.attach(
        f"Original Gender: {original_gender}\n"
        f"Updated Gender: {updated_gender}",
        name="Gender Test Data",
        attachment_type=allure.attachment_type.TEXT
    )

    try:
        with allure.step(f"Update gender to {updated_gender}"):
            my_info_page.select_gender(updated_gender)
            my_info_page.save_personal_details()

        with allure.step("Verify success message is displayed after gender update"):
            assert my_info_page.is_success_message_displayed(), (
                "Success message was not displayed after updating gender"
            )

        with allure.step("Verify updated gender is selected correctly"):
            assert my_info_page.get_selected_gender() == updated_gender, (
                "Updated gender was not selected correctly"
            )

            allure.attach(
                f"Selected Gender After Update: {my_info_page.get_selected_gender()}",
                name="Updated Gender Evidence",
                attachment_type=allure.attachment_type.TEXT
            )

    finally:
        with allure.step("Restore original gender selection"):
            if original_gender:
                my_info_page.select_gender(original_gender)
                my_info_page.save_personal_details()