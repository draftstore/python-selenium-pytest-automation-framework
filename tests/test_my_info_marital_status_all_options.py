import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


@allure.feature("My Info")
@allure.story("Personal Details Marital Status Dropdown")
@allure.title("Verify user can select all available marital status options")
def test_user_can_select_all_available_marital_status_options(driver):
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
        my_info_page.wait_until_personal_details_page_is_loaded()

    with allure.step("Capture original marital status"):
        original_marital_status = my_info_page.get_marital_status_value()

        allure.attach(
            f"Original Marital Status: {original_marital_status}",
            name="Original Marital Status",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Get available marital status options dynamically"):
        available_options = my_info_page.get_marital_status_options()

        testable_options = [
            option for option in available_options
            if option and option != "-- Select --"
        ]

        allure.attach(
            "\n".join(testable_options),
            name="Available Marital Status Options",
            attachment_type=allure.attachment_type.TEXT
        )

        assert testable_options, (
            "No selectable marital status options were found"
        )

    try:
        for status in testable_options:
            with allure.step(f"Select marital status option: {status}"):
                my_info_page.update_marital_status(status)

                actual_selected_value = my_info_page.get_marital_status_value()

                assert actual_selected_value == status, (
                    f"Marital Status dropdown did not show selected value. "
                    f"Expected: {status}, Actual: {actual_selected_value}"
                )

            with allure.step(f"Save marital status option: {status}"):
                my_info_page.save_personal_details()

                assert my_info_page.is_success_message_displayed(), (
                    f"Success message was not displayed after saving marital status: {status}"
                )

                allure.attach(
                    f"Selected Marital Status: {status}\n"
                    f"Displayed Value After Selection: {actual_selected_value}",
                    name=f"Marital Status Evidence - {status}",
                    attachment_type=allure.attachment_type.TEXT
                )

    finally:
        with allure.step("Final cleanup: restore original marital status if selectable"):
            current_status = my_info_page.get_marital_status_value()

            if current_status != original_marital_status:
                restored = my_info_page.restore_marital_status(original_marital_status)

                if restored:
                    my_info_page.save_personal_details()

                    assert my_info_page.is_success_message_displayed(), (
                        "Success message was not displayed after restoring marital status"
                    )

                    restored_status = my_info_page.get_marital_status_value()

                    allure.attach(
                        f"Original Marital Status: {original_marital_status}\n"
                        f"Restored Marital Status: {restored_status}",
                        name="Marital Status Restore Evidence",
                        attachment_type=allure.attachment_type.TEXT
                    )

                else:
                    allure.attach(
                        f"Original value was '{original_marital_status}', "
                        f"but it was not available as a selectable dropdown option. "
                        f"Restore was skipped.",
                        name="Marital Status Restore Skipped Reason",
                        attachment_type=allure.attachment_type.TEXT
                    )