import allure

from pathlib import Path

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage
from datetime import datetime


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
        my_info_page.wait_until_add_attachment_form_is_displayed()

        assert my_info_page.is_add_attachment_form_displayed(), (
            "Add Attachment form was not displayed"
            "Add Attachment form was not displayed"
        )
    return my_info_page


def get_latest_two_attachment_images():
    attachments_folder = Path("test_data") / "attachments"
    allowed_extensions = {".jpg", ".jpeg", ".png"}

    assert (
        attachments_folder.exists()
    ), f"Attachments test data folder was not found: {attachments_folder}"

    image_files = [
        file
        for file in attachments_folder.iterdir()
        if file.is_file() and file.suffix.lower() in allowed_extensions
    ]

    image_files = sorted(
        image_files,
        key=lambda file: file.stat().st_mtime,
    )

    assert len(image_files) >= 2, (
        "At least 2 valid images are required for attachment edit test. "
        "Please add two JPG/PNG images below 1MB using the image selection script."
    )

    initial_image = image_files[-2].resolve()
    updated_image = image_files[-1].resolve()

    return initial_image, updated_image


@allure.feature("My Info")
@allure.story("Attachment Edit")
@allure.title("Verify user can replace attachment image and update comment")
def test_user_can_replace_attachment_image_and_update_comment(driver):
    initial_image_path, updated_image_path = get_latest_two_attachment_images()

    initial_file_name = initial_image_path.name
    updated_file_name = updated_image_path.name
    updated_comment = (
        f"Automation updated attachment comment "
        f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
    )

    my_info_page = open_add_attachment_form(driver)

    with allure.step("Attach selected test data file paths"):
        allure.attach(
            f"Initial Image: {initial_image_path}\n"
            f"Updated Image: {updated_image_path}\n"
            f"Updated Comment: {updated_comment}",
            name="Attachment Edit Test Data",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Upload initial image attachment without comment"):
        my_info_page.upload_attachment_file(str(initial_image_path))

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Initial Attachment Image Selected",
            attachment_type=allure.attachment_type.PNG,
        )

        my_info_page.save_attachment()

    with allure.step("Wait until initial attachment appears in table"):
        my_info_page.wait_until_attachment_file_is_displayed(initial_file_name)

        assert my_info_page.is_attachment_file_displayed(initial_file_name), (
            f"Initial attachment file was not displayed in table: "
            f"{initial_file_name}"
        )

        my_info_page.highlight_uploaded_attachment_file(initial_file_name)

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Initial Uploaded Attachment Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Open Edit Attachment form for uploaded file"):
        my_info_page.click_edit_attachment_by_file_name(initial_file_name)

        assert (
            my_info_page.is_edit_attachment_form_displayed()
        ), "Edit Attachment form was not displayed"

        my_info_page.highlight_edit_attachment_form_title()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Edit Attachment Form Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Replace image and update comment"):
        my_info_page.replace_attachment_file(str(updated_image_path))
        my_info_page.wait_until_attachment_file_input_contains(updated_file_name)

        my_info_page.replace_attachment_comment(updated_comment)

        my_info_page.highlight_attachment_comment_textarea()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Updated Image Selected And Comment Entered",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Save edited attachment"):
        my_info_page.save_edited_attachment()

    with allure.step("Wait until updated attachment details appear in table"):
        my_info_page.wait_until_attachment_file_is_displayed(updated_file_name)
        my_info_page.wait_until_attachment_comment_is_displayed(updated_comment)

    with allure.step(
        "Verify updated image and comment are displayed in attachment table"
    ):
        assert my_info_page.is_attachment_file_displayed(updated_file_name), (
            f"Updated attachment file was not displayed in table: "
            f"{updated_file_name}"
        )

        assert my_info_page.is_attachment_comment_displayed(updated_comment), (
            f"Updated attachment comment was not displayed in table: "
            f"{updated_comment}"
        )

        my_info_page.highlight_uploaded_attachment_file(updated_file_name)
        my_info_page.highlight_uploaded_attachment_comment(updated_comment)

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Updated Attachment File And Comment Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )
