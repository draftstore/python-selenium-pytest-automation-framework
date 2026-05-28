import time

import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage
from utils.config_reader import ConfigReader


@allure.feature("My Info")
@allure.story("Personal Details Gender Update")
@allure.title("Verify user can update gender from Male to Female and restore original selection")


def test_user_can_update_gender_from_male_to_female_and_restore(driver):
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

    with allure.step("Capture original gender"):
        original_gender = my_info_page.get_selected_gender()

        if original_gender != "Male":
             my_info_page.select_gender("Male")
             my_info_page.save_personal_details()
             original_gender = my_info_page.get_selected_gender()
             
        assert original_gender == "Male", (f"Gender precondition failed. Expected Male, but found: {original_gender}")

        allure.attach(
            f"Original Gender: {original_gender}",
            name="Original Gender",
            attachment_type=allure.attachment_type.TEXT
        )

    try:
        with allure.step("Update gender from Male to Female"):
            my_info_page.select_gender("Female")
            my_info_page.save_personal_details()

        with allure.step("Verify success message is displayed after gender update"):
            assert my_info_page.is_success_message_displayed(), (
                "Success message was not displayed after updating gender"
            )

        with allure.step("Verify Female gender is selected"):
            actual_gender_after_update = my_info_page.get_selected_gender()

            assert actual_gender_after_update == "Female", (
                f"Gender was not updated correctly. "
                f"Expected: Female, Actual: {actual_gender_after_update}"
            )

            allure.attach(
                f"Original Gender: {original_gender}\n"
                f"Updated Gender: {actual_gender_after_update}",
                name="Gender Update Evidence",
                attachment_type=allure.attachment_type.TEXT
            )

        visual_pause = ConfigReader.get_visual_validation_pause()

        if visual_pause > 0:
            time.sleep(visual_pause)

    finally:
        with allure.step("Restore gender back to Male"):
            my_info_page.select_gender("Male")
            my_info_page.save_personal_details()

            restored_gender = my_info_page.get_selected_gender()

            assert restored_gender == "Male", (
                f"Gender was not restored correctly. "
                f"Expected: Male, Actual: {restored_gender}"
            )

            allure.attach(
                f"Gender After Restore: {restored_gender}",
                name="Gender Restore Evidence",
                attachment_type=allure.attachment_type.TEXT
            )

            visual_pause = ConfigReader.get_visual_validation_pause()

            if visual_pause > 0:
                time.sleep(visual_pause)