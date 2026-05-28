import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


@allure.feature("My Info")
@allure.story("Personal Details Nationality Dropdown")
@allure.title("Verify user can select all available nationality options dynamically")
def test_user_can_select_all_available_nationality_options(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    my_info_page = MyInfoPage(driver)

    # Fast mode for long dynamic dropdown validation
    login_page.slow_mode = 2
    dashboard_page.slow_mode = 2
    my_info_page.slow_mode = 2

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

    with allure.step("Capture original nationality"):
        original_nationality = my_info_page.get_nationality_value()

        allure.attach(
            f"Original Nationality: {original_nationality}",
            name="Original Nationality",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Get available nationality options dynamically"):
        available_options = my_info_page.get_nationality_options()

        testable_options = [
            option for option in available_options
            if option and option != "-- Select --"
        ]

        allure.attach(
            "\n".join(testable_options),
            name="Available Nationality Options",
            attachment_type=allure.attachment_type.TEXT
        )

        assert testable_options, (
            "No selectable nationality options were found"
        )

    try:
        for nationality in testable_options:
            with allure.step(f"Select nationality option: {nationality}"):
                my_info_page.update_nationality(nationality)

                actual_selected_value = my_info_page.get_nationality_value()

                assert actual_selected_value == nationality, (
                    f"Nationality dropdown did not show selected value. "
                    f"Expected: {nationality}, Actual: {actual_selected_value}"
                )

            with allure.step(f"Save nationality option: {nationality}"):
                my_info_page.save_personal_details()

                assert my_info_page.is_success_message_displayed(), (
                    f"Success message was not displayed after saving nationality: {nationality}"
                )

                allure.attach(
                    f"Selected Nationality: {nationality}\n"
                    f"Displayed Value After Selection: {actual_selected_value}",
                    name=f"Nationality Evidence - {nationality}",
                    attachment_type=allure.attachment_type.TEXT
                )

    finally:
        with allure.step("Final cleanup: restore original nationality if selectable"):
            current_nationality = my_info_page.get_nationality_value()

            if current_nationality != original_nationality:
                restored = my_info_page.restore_nationality(original_nationality)

                if restored:
                    my_info_page.save_personal_details()

                    assert my_info_page.is_success_message_displayed(), (
                        "Success message was not displayed after restoring nationality"
                    )

                    restored_nationality = my_info_page.get_nationality_value()

                    allure.attach(
                        f"Original Nationality: {original_nationality}\n"
                        f"Restored Nationality: {restored_nationality}",
                        name="Nationality Restore Evidence",
                        attachment_type=allure.attachment_type.TEXT
                    )

                else:
                    allure.attach(
                        f"Original value was '{original_nationality}', "
                        f"but it was not available as a selectable dropdown option. "
                        f"Restore was skipped.",
                        name="Nationality Restore Skipped Reason",
                        attachment_type=allure.attachment_type.TEXT
                    )