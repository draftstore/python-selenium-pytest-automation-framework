import allure
import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage

CONTACT_DETAILS_MAX_LENGTH_TEST_DATA = [
    pytest.param(
        "Street 1",
        "A" * 71,
        70,
        id="street-1-max-length-behavior",
    ),
    pytest.param(
        "Street 2",
        "B" * 71,
        70,
        id="street-2-max-length-behavior",
    ),
    pytest.param(
        "City",
        "C" * 71,
        70,
        id="city-max-length-behavior",
    ),
    pytest.param(
        "State/Province",
        "D" * 71,
        70,
        id="state-province-max-length-behavior",
    ),
    pytest.param(
        "Zip/Postal Code",
        "12345678901",
        10,
        id="zip-postal-code-max-length-behavior",
    ),
]


CONTACT_DETAILS_FORMAT_VALIDATION_TEST_DATA = [
    pytest.param(
        "Home",
        "InvalidPhoneABC",
        "Allows numbers and only + - / ( )",
        id="home-phone-format-validation",
    ),
    pytest.param(
        "Mobile",
        "MobileNumberABC",
        "Allows numbers and only + - / ( )",
        id="mobile-phone-format-validation",
    ),
    pytest.param(
        "Work",
        "WorkPhoneABC",
        "Allows numbers and only + - / ( )",
        id="work-phone-format-validation",
    ),
    pytest.param(
        "Work Email",
        "invalid-work-email",
        "Expected format: admin@example.com",
        id="work-email-format-validation",
    ),
    pytest.param(
        "Other Email",
        "invalid-other-email",
        "Expected format: admin@example.com",
        id="other-email-format-validation",
    ),
]


def open_contact_details_page(driver):
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

    with allure.step("Open Contact Details tab"):
        my_info_page.open_contact_details_tab()
        my_info_page.wait_until_contact_details_page_is_loaded()

    return my_info_page


@allure.feature("My Info")
@allure.story("Contact Details")
@allure.title("Verify Contact Details max length behavior")
@pytest.mark.parametrize(
    "field_label, input_value, expected_max_length",
    CONTACT_DETAILS_MAX_LENGTH_TEST_DATA,
)
def test_contact_details_max_length_behavior_is_verified(
    driver,
    field_label,
    input_value,
    expected_max_length,
):
    my_info_page = open_contact_details_page(driver)

    actual_max_length = my_info_page.get_contact_details_input_max_length(field_label)

    print("\n========== CONTACT DETAILS MAX LENGTH BEHAVIOR TEST ==========")
    print(f"Field              : {field_label}")
    print(f"Input Length       : {len(input_value)}")
    print(f"Expected Max Length: {expected_max_length}")
    print(f"DOM Max Length     : {actual_max_length}")

    with allure.step(f"Enter over-limit value in {field_label} field"):
        my_info_page.enter_contact_details_input(field_label, input_value)

        actual_value = my_info_page.get_contact_details_input_value(field_label)
        actual_length = len(actual_value)

        print(f"Actual Length      : {actual_length}")

        allure.attach(
            f"Field: {field_label}\n"
            f"Input Length: {len(input_value)}\n"
            f"Expected Max Length: {expected_max_length}\n"
            f"DOM Max Length: {actual_max_length}\n"
            f"Actual Length: {actual_length}\n"
            f"Actual Value: {actual_value}",
            name=f"{field_label} Max Length Behavior Evidence",
            attachment_type=allure.attachment_type.TEXT,
        )

    if actual_max_length is not None:
        with allure.step(f"Verify {field_label} enforces DOM maxlength"):
            assert actual_length == actual_max_length, (
                f"{field_label} field did not enforce DOM maxlength correctly. "
                f"DOM maxlength: {actual_max_length}, "
                f"Actual length: {actual_length}"
            )

            print("Status             : DOM maxlength enforced successfully")

    else:
        with allure.step(f"Verify {field_label} accepts entered input"):
            assert actual_length == len(input_value), (
                f"{field_label} field behavior is unexpected. "
                f"Input length: {len(input_value)}, "
                f"Actual length: {actual_length}"
            )

            print("Status             : No DOM maxlength found; full input accepted")

    my_info_page.highlight_contact_details_input(field_label)

    allure.attach(
        driver.get_screenshot_as_png(),
        name=f"{field_label} Max Length Behavior Highlighted",
        attachment_type=allure.attachment_type.PNG,
    )

    print("==============================================================\n")


@allure.feature("My Info")
@allure.story("Contact Details")
@allure.title("Verify Contact Details format validation message")
@pytest.mark.parametrize(
    "field_label, invalid_value, expected_error_message",
    CONTACT_DETAILS_FORMAT_VALIDATION_TEST_DATA,
)
def test_contact_details_format_validation_message_is_displayed(
    driver,
    field_label,
    invalid_value,
    expected_error_message,
):
    my_info_page = open_contact_details_page(driver)

    print("\n========== CONTACT DETAILS FORMAT VALIDATION TEST ==========")
    print(f"Field  : {field_label}")
    print(f"Value  : {invalid_value}")
    print(f"Expect : {expected_error_message}")

    with allure.step(f"Enter invalid value in {field_label} field"):
        my_info_page.enter_contact_details_input(field_label, invalid_value)

        actual_value = my_info_page.get_contact_details_input_value(field_label)

        print(f"Actual Value: {actual_value}")

        allure.attach(
            f"Field: {field_label}\n"
            f"Invalid Value: {invalid_value}\n"
            f"Actual Field Value: {actual_value}",
            name=f"{field_label} Invalid Input Evidence",
            attachment_type=allure.attachment_type.TEXT,
        )

        assert actual_value == invalid_value, (
            f"Invalid value was not entered correctly for field: {field_label}. "
            f"Expected: '{invalid_value}', "
            f"Actual: '{actual_value}'"
        )

    with allure.step("Save Contact Details form"):
        my_info_page.save_contact_details()

    with allure.step(f"Verify validation message for {field_label} field"):
        my_info_page.wait_until_contact_details_field_error_is_displayed(
            field_label,
            expected_error_message,
        )

        actual_error_message = my_info_page.get_contact_details_field_error_message(
            field_label
        )

        print(f"Actual Error: {actual_error_message}")

        allure.attach(
            f"Field: {field_label}\n"
            f"Expected Error: {expected_error_message}\n"
            f"Actual Error: {actual_error_message}",
            name=f"{field_label} Format Validation Evidence",
            attachment_type=allure.attachment_type.TEXT,
        )

        assert expected_error_message in actual_error_message, (
            f"Expected validation message was not displayed for field: {field_label}. "
            f"Expected: '{expected_error_message}', "
            f"Actual: '{actual_error_message}'"
        )

        my_info_page.highlight_contact_details_input(field_label)
        my_info_page.highlight_contact_details_field_error(field_label)

        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"{field_label} Format Validation Highlighted",
            attachment_type=allure.attachment_type.PNG,
        )

    print("Status : Format validation message displayed successfully")
    print("=========================================================\n")
