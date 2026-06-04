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
        my_info_page.wait_until_add_attachment_form_is_displayed()

        assert (
            my_info_page.is_add_attachment_form_displayed()
        ), "Add Attachment form was not displayed"

    return my_info_page


def get_latest_attachment_image():
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

    assert image_files, (
        "No valid attachment image was found. "
        "Please add at least one JPG/PNG image below 1MB using the image selection script."
    )

    latest_image = max(image_files, key=lambda file: file.stat().st_mtime)

    return latest_image.resolve()


@allure.feature("My Info")
@allure.story("Attachment Delete")
@allure.title("Verify user can delete an uploaded attachment")
def test_user_can_delete_uploaded_attachment(driver):
    attachment_file_path = get_latest_attachment_image()
    attachment_file_name = attachment_file_path.name

    my_info_page = open_add_attachment_form(driver)

    with allure.step("Attach selected test data file path"):
        allure.attach(
            str(attachment_file_path),
            name="Attachment Delete Test Data",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Upload attachment before delete"):
        my_info_page.upload_attachment_file(str(attachment_file_path))

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Attachment Selected Before Delete Test",
            attachment_type=allure.attachment_type.PNG,
        )

        my_info_page.save_attachment()

    with allure.step("Verify uploaded attachment appears in table"):
        my_info_page.wait_until_attachment_file_is_displayed(attachment_file_name)

        assert my_info_page.is_attachment_file_displayed(attachment_file_name), (
            f"Attachment file was not displayed before delete: "
            f"{attachment_file_name}"
        )

        my_info_page.highlight_uploaded_attachment_file(attachment_file_name)

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Uploaded Attachment Highlighted Before Delete",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Click Delete button for uploaded attachment"):
        my_info_page.highlight_delete_attachment_button_by_file_name(
            attachment_file_name
        )

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Delete Button Highlighted Before Click",
            attachment_type=allure.attachment_type.PNG,
        )

        my_info_page.click_delete_attachment_by_file_name(attachment_file_name)

    with allure.step("Verify delete confirmation modal is displayed"):
        assert (
            my_info_page.is_delete_attachment_confirmation_modal_displayed()
        ), "Delete confirmation modal was not displayed"

        my_info_page.highlight_delete_attachment_confirmation_modal()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Delete Confirmation Modal Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Confirm attachment delete"):
        my_info_page.confirm_delete_attachment()

    with allure.step("Verify attachment is removed from table"):
        my_info_page.wait_until_attachment_file_is_removed(attachment_file_name)

        assert not my_info_page.is_attachment_file_displayed(attachment_file_name), (
            f"Attachment file was still displayed after delete: "
            f"{attachment_file_name}"
        )

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Attachment Removed From Table",
            attachment_type=allure.attachment_type.PNG,
        )
