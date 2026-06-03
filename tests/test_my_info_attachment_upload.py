import allure

from pathlib import Path

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


def open_add_attachment_form(driver):
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

    with allure.step("Open Add Attachment form"):
        assert (
            my_info_page.is_add_attachment_button_displayed()
        ), "Add Attachment button was not displayed"

        my_info_page.click_add_attachment_button()

        assert (
            my_info_page.is_add_attachment_form_displayed()
        ), "Add Attachment form was not displayed"

    return my_info_page


@allure.feature("My Info")
@allure.story("Attachment Upload")
@allure.title("Verify user can upload a valid image attachment without comment")
def test_user_can_upload_valid_image_attachment_without_comment(driver):
    my_info_page = open_add_attachment_form(driver)

    attachment_file_path = (
        Path("test_data") / "attachments" / "orangehrm_attachment_test_image.jpg"
    ).resolve()

    attachment_file_name = attachment_file_path.name

    with allure.step("Verify attachment test image exists"):
        assert (
            attachment_file_path.exists()
        ), f"Attachment test image was not found: {attachment_file_path}"

        allure.attach(
            str(attachment_file_path),
            name="Attachment File Path",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Upload valid image attachment"):
        my_info_page.upload_attachment_file(str(attachment_file_path))

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Attachment Image Selected",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Save uploaded attachment"):
        assert (
            my_info_page.is_attachment_save_button_displayed()
        ), "Attachment Save button was not displayed"

        my_info_page.highlight_attachment_save_button()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Attachment Save Button Highlighted Before Upload",
            attachment_type=allure.attachment_type.PNG,
        )

        my_info_page.save_attachment()

    with allure.step("Wait until uploaded attachment appears in table"):
        my_info_page.wait_until_attachment_file_is_displayed(attachment_file_name)

    with allure.step("Verify uploaded file is displayed in attachment table"):
        assert my_info_page.is_attachment_file_displayed(attachment_file_name), (
            f"Uploaded attachment file was not displayed in table: "
            f"{attachment_file_name}"
        )

        my_info_page.highlight_uploaded_attachment_file(attachment_file_name)

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Uploaded Attachment File Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )
