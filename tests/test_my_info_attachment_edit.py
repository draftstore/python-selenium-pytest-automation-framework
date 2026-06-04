import allure
import shutil
import hashlib

from pathlib import Path
from datetime import datetime

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


def get_file_hash(file_path: Path):
    return hashlib.sha256(file_path.read_bytes()).hexdigest()


def get_latest_two_different_attachment_images():
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
        reverse=True,
    )

    assert len(image_files) >= 2, (
        "At least 2 valid images are required for attachment edit test. "
        "Please add two different JPG/PNG images below 1MB."
    )

    latest_image = image_files[0]
    latest_image_hash = get_file_hash(latest_image)

    for candidate_image in image_files[1:]:
        if get_file_hash(candidate_image) != latest_image_hash:
            return candidate_image.resolve(), latest_image.resolve()

    raise AssertionError(
        "Attachment edit test requires two different images by content. "
        "Current images appear to have the same content. "
        "Please upload/select another different JPG/PNG image below 1MB."
    )


def create_unique_attachment_file(source_file: Path, prefix: str, timestamp: str):
    unique_file_name = f"{prefix}_{timestamp}{source_file.suffix.lower()}"
    unique_file_path = source_file.parent / unique_file_name

    shutil.copy2(source_file, unique_file_path)

    return unique_file_path.resolve()


def get_allure_image_attachment_type(image_path: Path):
    extension = image_path.suffix.lower()

    if extension in [".jpg", ".jpeg"]:
        return allure.attachment_type.JPG

    if extension == ".png":
        return allure.attachment_type.PNG

    return allure.attachment_type.TEXT


@allure.feature("My Info")
@allure.story("Attachment Edit")
@allure.title("Verify user can replace attachment image and update comment")
def test_user_can_replace_attachment_image_and_update_comment(driver):
    source_initial_image_path, source_updated_image_path = (
        get_latest_two_different_attachment_images()
    )

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    initial_image_path = create_unique_attachment_file(
        source_initial_image_path,
        "Edit_Initial_Image",
        timestamp,
    )

    updated_image_path = create_unique_attachment_file(
        source_updated_image_path,
        "Edit_Updated_Image",
        timestamp,
    )

    initial_file_name = initial_image_path.name
    updated_file_name = updated_image_path.name

    initial_comment = f"Automation initial attachment comment {timestamp}"
    updated_comment = f"Automation updated attachment comment {timestamp}"

    my_info_page = open_add_attachment_form(driver)

    with allure.step("Attach selected test data files"):
        allure.attach(
            f"Source Initial Image: {source_initial_image_path}\n"
            f"Source Updated Image: {source_updated_image_path}\n"
            f"Unique Initial Image: {initial_image_path}\n"
            f"Unique Updated Image: {updated_image_path}\n"
            f"Initial Comment: {initial_comment}\n"
            f"Updated Comment: {updated_comment}",
            name="Attachment Edit Test Data",
            attachment_type=allure.attachment_type.TEXT,
        )

        allure.attach.file(
            str(initial_image_path),
            name="Initial Attachment Image",
            attachment_type=get_allure_image_attachment_type(initial_image_path),
        )

        allure.attach.file(
            str(updated_image_path),
            name="Updated Attachment Image",
            attachment_type=get_allure_image_attachment_type(updated_image_path),
        )

    with allure.step("Upload initial image attachment with initial comment"):
        my_info_page.upload_attachment_file(str(initial_image_path))
        my_info_page.enter_attachment_comment(initial_comment)

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Initial Attachment Image Selected With Comment",
            attachment_type=allure.attachment_type.PNG,
        )

        my_info_page.save_attachment()

    with allure.step("Verify initial attachment file and comment are saved in table"):
        my_info_page.wait_until_attachment_file_is_displayed(initial_file_name)
        my_info_page.wait_until_attachment_comment_is_displayed(initial_comment)

        initial_row_text = my_info_page.get_attachment_row_by_file_name(
            initial_file_name
        ).text

        allure.attach(
            initial_row_text,
            name="Initial Attachment Row Text",
            attachment_type=allure.attachment_type.TEXT,
        )

        assert initial_file_name in initial_row_text, (
            f"Initial file name was not found in row. "
            f"Expected: '{initial_file_name}', "
            f"Row Text: '{initial_row_text}'"
        )

        assert initial_comment in initial_row_text, (
            f"Initial comment was not found in row. "
            f"Expected: '{initial_comment}', "
            f"Row Text: '{initial_row_text}'"
        )

        my_info_page.highlight_uploaded_attachment_file(initial_file_name)
        my_info_page.highlight_uploaded_attachment_comment(initial_comment)

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Initial Uploaded Attachment And Comment Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Open Edit Attachment form for the exact uploaded row"):
        my_info_page.click_edit_attachment_by_file_name_and_comment(
            initial_file_name,
            initial_comment,
        )

        assert (
            my_info_page.is_edit_attachment_form_displayed()
        ), "Edit Attachment form was not displayed"

        my_info_page.wait_until_edit_attachment_current_file_is(initial_file_name)

        current_file_before_replace = (
            my_info_page.get_edit_attachment_current_file_name()
        )

        assert current_file_before_replace == initial_file_name, (
            f"Edit form opened for wrong attachment. "
            f"Expected current file: '{initial_file_name}', "
            f"Actual current file: '{current_file_before_replace}'"
        )

        allure.attach(
            f"Current File In Edit Form: {current_file_before_replace}",
            name="Edit Attachment Current File Before Replace",
            attachment_type=allure.attachment_type.TEXT,
        )

        my_info_page.highlight_edit_attachment_form_title()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Edit Attachment Form Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Replace image and update comment before save"):
        current_file_before_replace = (
            my_info_page.get_edit_attachment_current_file_name()
        )

        allure.attach(
            f"Current File Before Replace: {current_file_before_replace}\n"
            f"Expected Updated File: {updated_file_name}",
            name="Edit Attachment File Replace Evidence",
            attachment_type=allure.attachment_type.TEXT,
        )

        my_info_page.replace_attachment_file(str(updated_image_path))
        my_info_page.wait_until_edit_attachment_selected_file_is(updated_file_name)
        my_info_page.wait_until_attachment_form_loader_disappears()

        my_info_page.replace_attachment_comment(updated_comment)

        actual_comment_before_save = my_info_page.get_attachment_comment_value()

        assert actual_comment_before_save == updated_comment, (
            f"Updated comment was not entered correctly before save. "
            f"Expected: '{updated_comment}', "
            f"Actual: '{actual_comment_before_save}'"
        )

        my_info_page.highlight_attachment_comment_textarea()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Updated Image Selected And Comment Updated Before Save",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Save edited attachment"):
        my_info_page.save_edited_attachment()

    with allure.step("Verify updated attachment row after save"):
        my_info_page.wait_until_attachment_file_is_displayed(updated_file_name)

        updated_row_text = my_info_page.get_attachment_row_by_file_name(
            updated_file_name
        ).text

        allure.attach(
            updated_row_text,
            name="Updated Attachment Row Text After Save",
            attachment_type=allure.attachment_type.TEXT,
        )

        assert updated_file_name in updated_row_text, (
            f"Updated file name was not found in row after save. "
            f"Expected: '{updated_file_name}', "
            f"Row Text: '{updated_row_text}'"
        )

        assert updated_comment in updated_row_text, (
            f"Updated comment was not found in the updated attachment row after save. "
            f"This means image was updated, but comment was not updated. "
            f"Expected Comment: '{updated_comment}', "
            f"Row Text: '{updated_row_text}'"
        )

        assert initial_comment not in updated_row_text, (
            f"Old comment is still displayed after editing attachment. "
            f"Old Comment: '{initial_comment}', "
            f"Row Text: '{updated_row_text}'"
        )

        my_info_page.highlight_attachment_row_by_file_name_and_comment(
            updated_file_name,
            updated_comment,
        )

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Updated Attachment Row Highlighted After Save",
            attachment_type=allure.attachment_type.PNG,
        )
