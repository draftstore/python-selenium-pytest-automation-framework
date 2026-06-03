import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


@allure.feature("My Info")
@allure.story("Attachments Section")
@allure.title("Verify Attachments section and Add button are displayed")
def test_attachments_section_and_add_button_are_displayed(driver):
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

    with allure.step("Verify Attachments section is displayed"):
        assert (
            my_info_page.is_attachments_heading_displayed()
        ), "Attachments heading was not displayed"

        my_info_page.highlight_attachments_heading()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Attachments Heading Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Verify Add Attachment button is displayed"):
        assert (
            my_info_page.is_add_attachment_button_displayed()
        ), "Add Attachment button was not displayed"

        my_info_page.highlight_add_attachment_button()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Add Attachment Button Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )


@allure.feature("My Info")
@allure.story("Attachments Section")
@allure.title("Verify Add Attachment form is displayed after clicking Add")
def test_add_attachment_form_is_displayed_after_clicking_add(driver):
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

    with allure.step("Click Add Attachment button"):
        assert (
            my_info_page.is_add_attachment_button_displayed()
        ), "Add Attachment button was not displayed"

        my_info_page.highlight_add_attachment_button()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Add Attachment Button Highlighted Before Click",
            attachment_type=allure.attachment_type.PNG,
        )

        my_info_page.click_add_attachment_button()

    with allure.step("Verify Add Attachment form is displayed"):
        assert (
            my_info_page.is_add_attachment_form_displayed()
        ), "Add Attachment form was not displayed"

        my_info_page.highlight_add_attachment_form_title()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Add Attachment Form Title Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Verify Add Attachment form fields and buttons are displayed"):
        assert (
            my_info_page.is_attachment_select_file_label_displayed()
        ), "Select File label was not displayed"

        assert (
            my_info_page.is_attachment_browse_button_displayed()
        ), "Browse button was not displayed"

        assert (
            my_info_page.is_attachment_comment_textarea_displayed()
        ), "Comment textarea was not displayed"

        assert (
            my_info_page.is_attachment_file_size_hint_displayed()
        ), "File size hint was not displayed"

        assert (
            my_info_page.is_attachment_cancel_button_displayed()
        ), "Cancel button was not displayed"

        assert (
            my_info_page.is_attachment_save_button_displayed()
        ), "Save button was not displayed"

        my_info_page.highlight_attachment_browse_button()
        my_info_page.highlight_attachment_comment_textarea()
        my_info_page.highlight_attachment_cancel_button()
        my_info_page.highlight_attachment_save_button()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Add Attachment Form Fields Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )
