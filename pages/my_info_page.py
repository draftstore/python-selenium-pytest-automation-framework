from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

from pages.base_page import BasePage


class MyInfoPage(BasePage):
    """
    Page Object Model class for OrangeHRM My Info > Personal Details page.
    """

    # Sidebar Menu
    MY_INFO_MENU = (By.XPATH, "//span[normalize-space()='My Info']")

    # Page Header / Tab
    PERSONAL_DETAILS_HEADER = (By.XPATH, "//h6[normalize-space()='Personal Details']")
    PERSONAL_DETAILS_TAB = (By.XPATH, "//a[normalize-space()='Personal Details']")

    # Name Section
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    MIDDLE_NAME_INPUT = (By.NAME, "middleName")
    LAST_NAME_INPUT = (By.NAME, "lastName")

    FIRST_NAME_ERROR_MESSAGE = (
        By.XPATH,
        "//input[@name='firstName']"
        "/ancestor::div[contains(@class,'oxd-input-field-bottom-space')]"
        "//span[contains(@class,'oxd-input-field-error-message')]",
    )

    MIDDLE_NAME_ERROR_MESSAGE = (
        By.XPATH,
        "//input[@name='middleName']"
        "/ancestor::div[contains(@class,'oxd-input-field-bottom-space')]"
        "//span[contains(@class,'oxd-input-field-error-message')]",
    )

    LAST_NAME_ERROR_MESSAGE = (
        By.XPATH,
        "//input[@name='lastName']"
        "/ancestor::div[contains(@class,'oxd-input-field-bottom-space')]"
        "//span[contains(@class,'oxd-input-field-error-message')]",
    )

    # ID Section
    EMPLOYEE_ID_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Employee Id']"
        "/ancestor::div[contains(@class,'oxd-input-group')]//input",
    )

    OTHER_ID_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Other Id']"
        "/ancestor::div[contains(@class,'oxd-input-group')]//input",
    )

    DRIVERS_LICENSE_INPUT = (
        By.XPATH,
        '//label[normalize-space()="Driver\'s License Number"]'
        "/ancestor::div[contains(@class,'oxd-input-group')]//input",
    )

    EMPLOYEE_ID_ERROR_MESSAGE = (
        By.XPATH,
        "//label[normalize-space()='Employee Id']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//span[contains(@class,'oxd-input-field-error-message')]",
    )

    OTHER_ID_ERROR_MESSAGE = (
        By.XPATH,
        "//label[normalize-space()='Other Id']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//span[contains(@class,'oxd-input-field-error-message')]",
    )

    DRIVERS_LICENSE_ERROR_MESSAGE = (
        By.XPATH,
        '//label[normalize-space()="Driver\'s License Number"]'
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//span[contains(@class,'oxd-input-field-error-message')]",
    )

    LICENSE_EXPIRY_DATE_INPUT = (
        By.XPATH,
        "(//input[@placeholder='yyyy-dd-mm'])[1]",
    )

    DATE_OF_BIRTH_INPUT = (
        By.XPATH,
        "(//input[@placeholder='yyyy-dd-mm'])[2]",
    )

    LICENSE_EXPIRY_DATE_ICON = (
        By.XPATH,
        "((//input[@placeholder='yyyy-dd-mm'])[1]"
        "/ancestor::div[contains(@class,'oxd-date-input')]"
        "//i[contains(@class,'bi-calendar')])[1]",
    )

    DATE_OF_BIRTH_ICON = (
        By.XPATH,
        "((//input[@placeholder='yyyy-dd-mm'])[2]"
        "/ancestor::div[contains(@class,'oxd-date-input')]"
        "//i[contains(@class,'bi-calendar')])[1]",
    )

    # Personal Information Section
    NATIONALITY_DROPDOWN = (
        By.XPATH,
        "//label[normalize-space()='Nationality']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]",
    )

    MARITAL_STATUS_DROPDOWN = (
        By.XPATH,
        "//label[normalize-space()='Marital Status']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]",
    )

    MALE_RADIO_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Male']//input[@type='radio']",
    )

    FEMALE_RADIO_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Female']//input[@type='radio']",
    )

    MALE_RADIO_CLICK_TARGET = (
        By.XPATH,
        "//label[normalize-space()='Male']//span[contains(@class,'oxd-radio-input')]",
    )

    FEMALE_RADIO_CLICK_TARGET = (
        By.XPATH,
        "//label[normalize-space()='Female']//span[contains(@class,'oxd-radio-input')]",
    )

    # Save Button
    PERSONAL_DETAILS_SAVE_BUTTON = (
        By.XPATH,
        "//label[normalize-space()='Marital Status']"
        "/ancestor::form//button[@type='submit' and normalize-space()='Save']",
    )

    # Custom Fields Section
    BLOOD_TYPE_DROPDOWN = (
        By.XPATH,
        "//label[normalize-space()='Blood Type']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]",
    )

    TEST_FIELD_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Test_Field']"
        "/ancestor::div[contains(@class,'oxd-input-group')]//input",
    )

    TEST_FIELD_ERROR_MESSAGE = (
        By.XPATH,
        "//label[normalize-space()='Test_Field']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//span[contains(@class,'oxd-input-field-error-message')]",
    )

    CUSTOM_FIELDS_SAVE_BUTTON = (
        By.XPATH,
        "//label[normalize-space()='Blood Type']"
        "/ancestor::form//button[@type='submit' and normalize-space()='Save']",
    )

    # Attachments Section
    ATTACHMENTS_HEADING = (
        By.XPATH,
        "//h6[normalize-space()='Attachments']",
    )

    ADD_ATTACHMENT_BUTTON = (
        By.XPATH,
        "//h6[normalize-space()='Attachments']"
        "/following::button[normalize-space()='Add'][1]",
    )

    ADD_ATTACHMENT_FORM_TITLE = (
        By.XPATH,
        "//h6[normalize-space()='Add Attachment']",
    )

    ATTACHMENT_SELECT_FILE_LABEL = (
        By.XPATH,
        "//label[normalize-space()='Select File']",
    )

    ATTACHMENT_BROWSE_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'oxd-file-button') and normalize-space()='Browse']",
    )

    ATTACHMENT_COMMENT_TEXTAREA = (
        By.XPATH,
        "//textarea[@placeholder='Type comment here']",
    )

    ATTACHMENT_CANCEL_BUTTON = (
        By.XPATH,
        "//h6[normalize-space()='Add Attachment']"
        "/following::button[@type='button' and normalize-space()='Cancel'][1]",
    )

    ATTACHMENT_SAVE_BUTTON = (
        By.XPATH,
        "//h6[normalize-space()='Add Attachment']"
        "/following::button[@type='submit' and normalize-space()='Save'][1]",
    )

    ATTACHMENT_FILE_SIZE_HINT = (
        By.XPATH,
        "//p[normalize-space()='Accepts up to 1MB']",
    )

    ATTACHMENT_FILE_REQUIRED_ERROR_MESSAGE = (
        By.XPATH,
        "//label[normalize-space()='Select File']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//span[contains(@class,'oxd-input-field-error-message')]",
    )

    ATTACHMENT_COMMENT_ERROR_MESSAGE = (
        By.XPATH,
        "//label[normalize-space()='Comment']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//span[contains(@class,'oxd-input-field-error-message')]",
    )

    ATTACHMENT_FILE_INPUT = (
        By.XPATH,
        "//input[@type='file']",
    )

    ATTACHMENT_TABLE_ROWS = (
        By.XPATH,
        "//h6[normalize-space()='Attachments']"
        "/following::div[contains(@class,'oxd-table-body')][1]"
        "//div[contains(@class,'oxd-table-card')]",
    )

    EDIT_ATTACHMENT_FORM_TITLE = (
        By.XPATH,
        "//h6[normalize-space()='Edit Attachment']",
    )

    EDIT_ATTACHMENT_SAVE_BUTTON = (
        By.XPATH,
        "//h6[normalize-space()='Edit Attachment']"
        "/following::button[@type='submit' and normalize-space()='Save'][1]",
    )

    DELETE_ATTACHMENT_CONFIRMATION_MODAL = (
        By.XPATH,
        "//p[normalize-space()='Are you Sure?']",
    )

    CONFIRM_DELETE_ATTACHMENT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Yes, Delete']",
    )

    CANCEL_DELETE_ATTACHMENT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='No, Cancel']",
    )

    ATTACHMENT_FORM_LOADER = (
        By.XPATH,
        "//div[contains(@class,'oxd-form-loader')]",
    )

    EDIT_ATTACHMENT_CURRENT_FILE_TEXT = (
        By.XPATH,
        "//h6[normalize-space()='Edit Attachment']"
        "/following::label[normalize-space()='Current File'][1]"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//p[contains(@class,'oxd-text--p')]",
    )

    EDIT_ATTACHMENT_REPLACE_FILE_INPUT = (
        By.XPATH,
        "//h6[normalize-space()='Edit Attachment']"
        "/following::label[normalize-space()='Replace With'][1]"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input[@type='file']",
    )

    EDIT_ATTACHMENT_SELECTED_FILE_TEXT = (
        By.XPATH,
        "//h6[normalize-space()='Edit Attachment']"
        "/following::label[normalize-space()='Replace With'][1]"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-file-input-div')]",
    )

    def open_my_info_page(self):
        self.click(self.MY_INFO_MENU)

    def is_personal_details_page_displayed(self):
        return self.is_element_visible(self.PERSONAL_DETAILS_HEADER)

    def get_first_name_value(self):
        return self.get_attribute(self.FIRST_NAME_INPUT, "value")

    def get_middle_name_value(self):
        return self.get_attribute(self.MIDDLE_NAME_INPUT, "value")

    def get_last_name_value(self):
        return self.get_attribute(self.LAST_NAME_INPUT, "value")

    def get_employee_id_value(self):
        return self.get_attribute(self.EMPLOYEE_ID_INPUT, "value")

    def get_other_id_value(self):
        return self.get_attribute(self.OTHER_ID_INPUT, "value")

    def are_name_fields_visible(self):
        return (
            self.find_element(self.FIRST_NAME_INPUT) is not None
            and self.find_element(self.MIDDLE_NAME_INPUT) is not None
            and self.find_element(self.LAST_NAME_INPUT) is not None
        )

    def are_id_fields_visible(self):
        return (
            self.is_element_visible(self.EMPLOYEE_ID_INPUT)
            and self.is_element_visible(self.OTHER_ID_INPUT)
            and self.is_element_visible(self.DRIVERS_LICENSE_INPUT)
            and self.is_element_visible(self.LICENSE_EXPIRY_DATE_INPUT)
        )

    def are_personal_information_fields_visible(self):
        return (
            self.is_element_visible(self.NATIONALITY_DROPDOWN)
            and self.is_element_visible(self.MARITAL_STATUS_DROPDOWN)
            and self.is_element_visible(self.DATE_OF_BIRTH_INPUT)
            and self.is_element_visible(self.MALE_RADIO_CLICK_TARGET)
            and self.is_element_visible(self.FEMALE_RADIO_CLICK_TARGET)
        )

    def is_save_button_visible(self):
        return self.is_element_visible(self.PERSONAL_DETAILS_SAVE_BUTTON)

    def get_drivers_license_value(self):
        return self.get_attribute(self.DRIVERS_LICENSE_INPUT, "value")

    def update_other_id(self, other_id: str):
        self.enter_text(self.OTHER_ID_INPUT, other_id)

    def update_drivers_license_number(self, license_number: str):
        self.enter_text(self.DRIVERS_LICENSE_INPUT, license_number)

    def save_personal_details(self):
        self.click(self.PERSONAL_DETAILS_SAVE_BUTTON)

    def is_success_message_displayed(self):
        success_message = (By.XPATH, "//p[normalize-space()='Successfully Updated']")
        return self.is_element_visible(success_message)

    def get_marital_status_value(self):
        return self.get_custom_dropdown_selected_text(self.MARITAL_STATUS_DROPDOWN)

    def update_marital_status(self, marital_status: str):
        self.select_custom_dropdown_option(self.MARITAL_STATUS_DROPDOWN, marital_status)

    def get_nationality_value(self):
        return self.get_custom_dropdown_selected_text(self.NATIONALITY_DROPDOWN)

    def get_nationality_options(self):
        return self.get_custom_dropdown_options(self.NATIONALITY_DROPDOWN)

    def update_nationality(self, nationality: str):
        self.select_custom_dropdown_option(self.NATIONALITY_DROPDOWN, nationality)

    def restore_nationality(self, original_value: str):
        if not original_value:
            return False
        if self.is_custom_dropdown_option_available(
            self.NATIONALITY_DROPDOWN, original_value
        ):
            self.update_nationality(original_value)
            return True
        return False

    def update_nationality_for_all_options_test(self, nationality: str):
        """
        Dedicated nationality selector for exhaustive all-options validation.
        This method does not affect the normal update_nationality() method.
        """

        option_locator = (
            By.XPATH,
            f"//div[@role='option'][.//span[normalize-space()="
            f"{self.get_xpath_text_literal(nationality)}]]",
        )

        last_error = None

        for _ in range(5):
            try:
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

                self.click(self.NATIONALITY_DROPDOWN)

                option = self.wait_for_clickable(option_locator)

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    option,
                )

                self.driver.execute_script(
                    """
                    arguments[0].dispatchEvent(
                        new MouseEvent('mousedown', { bubbles: true })
                    );
                    arguments[0].dispatchEvent(
                        new MouseEvent('mouseup', { bubbles: true })
                    );
                    arguments[0].click();
                    """,
                    option,
                )

                self.wait.until(lambda _: self.get_nationality_value() == nationality)

                return

            except (
                StaleElementReferenceException,
                TimeoutException,
                AssertionError,
            ) as error:
                last_error = error
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

        actual_value = self.get_nationality_value()

        raise AssertionError(
            f"Could not select nationality option after retries. "
            f"Expected: {nationality}, Actual: {actual_value}. "
            f"Last error: {last_error}"
        )

    def restore_nationality_for_all_options_test(self, original_value: str):
        """
        Restores original nationality using the dedicated all-options selector.
        """

        if not original_value or original_value == "-- Select --":
            return False

        self.update_nationality_for_all_options_test(original_value)
        return True

    def select_gender(self, gender: str):
        if gender == "Male":
            self.click(self.MALE_RADIO_CLICK_TARGET)
        elif gender == "Female":
            self.click(self.FEMALE_RADIO_CLICK_TARGET)
        else:
            raise ValueError(f"Unsupported gender option: {gender}")

    def get_selected_gender(self):
        male_radio = self.find_element(self.MALE_RADIO_INPUT)
        female_radio = self.find_element(self.FEMALE_RADIO_INPUT)
        is_male_selected = self.driver.execute_script(
            "return arguments[0].checked;", male_radio
        )

        is_female_selected = self.driver.execute_script(
            "return arguments[0].checked;", female_radio
        )

        if is_male_selected:
            return "Male"

        if is_female_selected:
            return "Female"
        return ""

    def wait_until_personal_details_page_is_loaded(self):
        self.wait_for_visible(self.PERSONAL_DETAILS_HEADER)
        self.wait_for_presence(self.FIRST_NAME_INPUT)
        self.wait_for_presence(self.MIDDLE_NAME_INPUT)
        self.wait_for_presence(self.LAST_NAME_INPUT)
        self.wait_for_presence(self.OTHER_ID_INPUT)

    def get_marital_status_options(self):
        return self.get_custom_dropdown_options(self.MARITAL_STATUS_DROPDOWN)

    def restore_marital_status(self, original_value: str):
        if not original_value:
            return False
        if self.is_custom_dropdown_option_available(
            self.MARITAL_STATUS_DROPDOWN, original_value
        ):
            self.update_marital_status(original_value)
            return True
        return False

    def get_date_of_birth_value(self):
        return self.get_attribute(self.DATE_OF_BIRTH_INPUT, "value") or ""

    def get_license_expiry_date_value(self):
        return self.get_attribute(self.LICENSE_EXPIRY_DATE_INPUT, "value") or ""

    def select_date_from_orangehrm_datepicker(
        self, calendar_icon_locator, date_value: str
    ):
        """
        Selects a date using OrangeHRM datepicker UI.

        Expected format: yyyy-dd-mm
        Example: 2001-15-05
        """

        year, day, month = date_value.split("-")

        month_names = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December",
        }

        month_name = month_names[month]

        self.click(calendar_icon_locator)

        month_dropdown = (
            By.XPATH,
            "//div[contains(@class,'oxd-calendar-selector-month-selected')]",
        )

        year_dropdown = (
            By.XPATH,
            "//div[contains(@class,'oxd-calendar-selector-year-selected')]",
        )

        self.click(month_dropdown)

        month_option = (
            By.XPATH,
            f"//li[contains(@class,'oxd-calendar-dropdown--option') "
            f"and normalize-space()='{month_name}']",
        )
        self.click(month_option)

        self.click(year_dropdown)

        year_option = (
            By.XPATH,
            f"//li[contains(@class,'oxd-calendar-dropdown--option') "
            f"and normalize-space()='{year}']",
        )
        self.click(year_option)

        day_option = (
            By.XPATH,
            f"//div[contains(@class,'oxd-calendar-date') "
            f"and not(contains(@class,'--non-current-month')) "
            f"and normalize-space()='{int(day)}']",
        )
        self.click(day_option)

        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

    def clear_date_input_field(self, date_input_locator):
        """
        Clears OrangeHRM date input field strictly and verifies blank value.
        """

        element = self.wait_for_visible(date_input_locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(Keys.BACKSPACE)

        self.driver.execute_script(
            """
            const element = arguments[0];

            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                window.HTMLInputElement.prototype,
                'value'
            ).set;

            nativeInputValueSetter.call(element, '');

            element.dispatchEvent(new Event('input', { bubbles: true }));
            element.dispatchEvent(new Event('change', { bubbles: true }));
            element.dispatchEvent(new KeyboardEvent('keydown', { bubbles: true }));
            element.dispatchEvent(new KeyboardEvent('keyup', { bubbles: true }));
            element.dispatchEvent(new Event('blur', { bubbles: true }));
            """,
            element,
        )

        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

        self.wait.until(
            lambda _: (self.get_attribute(date_input_locator, "value") or "") == ""
        )

    def update_date_of_birth(self, dob: str):
        self.select_date_from_orangehrm_datepicker(self.DATE_OF_BIRTH_ICON, dob)

    def update_license_expiry_date(self, expiry_date: str):
        self.select_date_from_orangehrm_datepicker(
            self.LICENSE_EXPIRY_DATE_ICON, expiry_date
        )

    def clear_date_of_birth(self):
        self.clear_date_input_field(self.DATE_OF_BIRTH_INPUT)

    def clear_license_expiry_date(self):
        self.clear_date_input_field(self.LICENSE_EXPIRY_DATE_INPUT)

    def wait_until_date_of_birth_value_is(self, expected_value: str):
        self.wait.until(lambda _: self.get_date_of_birth_value() == expected_value)

    def wait_until_license_expiry_date_value_is(self, expected_value: str):
        self.wait.until(
            lambda _: self.get_license_expiry_date_value() == expected_value
        )

    def is_date_of_birth_error_displayed(self):
        dob_error_message = (
            By.XPATH,
            "//label[normalize-space()='Date of Birth']"
            "/ancestor::div[contains(@class,'oxd-input-group')]"
            "//span[contains(@class,'oxd-input-field-error-message')]",
        )
        return self.is_element_visible(dob_error_message)

    def update_first_name(self, first_name: str):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)

    def update_middle_name(self, middle_name: str):
        self.enter_text(self.MIDDLE_NAME_INPUT, middle_name)

    def update_last_name(self, last_name: str):
        self.enter_text(self.LAST_NAME_INPUT, last_name)

    def restore_name_fields(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
    ):
        self.update_first_name(first_name)
        self.update_middle_name(middle_name)
        self.update_last_name(last_name)
        self.save_personal_details()

    def get_first_name_error_message(self):
        return self.get_text(self.FIRST_NAME_ERROR_MESSAGE)

    def get_middle_name_error_message(self):
        return self.get_text(self.MIDDLE_NAME_ERROR_MESSAGE)

    def get_last_name_error_message(self):
        return self.get_text(self.LAST_NAME_ERROR_MESSAGE)

    def is_first_name_error_displayed(self):
        return len(self.driver.find_elements(*self.FIRST_NAME_ERROR_MESSAGE)) > 0

    def is_middle_name_error_displayed(self):
        return len(self.driver.find_elements(*self.MIDDLE_NAME_ERROR_MESSAGE)) > 0

    def is_last_name_error_displayed(self):
        return len(self.driver.find_elements(*self.LAST_NAME_ERROR_MESSAGE)) > 0

    def update_employee_id(self, employee_id: str):
        self.enter_text(self.EMPLOYEE_ID_INPUT, employee_id)

    def get_employee_id_error_message(self):
        return self.get_text(self.EMPLOYEE_ID_ERROR_MESSAGE)

    def get_other_id_error_message(self):
        return self.get_text(self.OTHER_ID_ERROR_MESSAGE)

    def get_drivers_license_error_message(self):
        return self.get_text(self.DRIVERS_LICENSE_ERROR_MESSAGE)

    def restore_id_fields(
        self,
        employee_id: str,
        other_id: str,
        drivers_license_number: str,
    ):
        self.update_employee_id(employee_id)
        self.update_other_id(other_id)
        self.update_drivers_license_number(drivers_license_number)
        self.save_personal_details()

    def get_blood_type_value(self):
        return self.get_custom_dropdown_selected_text(self.BLOOD_TYPE_DROPDOWN)

    def get_blood_type_options(self):
        return self.get_custom_dropdown_options(self.BLOOD_TYPE_DROPDOWN)

    def update_blood_type(self, blood_type: str):
        """
        Selects Blood Type option using a dedicated retry-based method.
        This method is separate because this custom dropdown can refresh its DOM.
        """

        option_locator = (
            By.XPATH,
            f"//div[@role='option'][.//span[normalize-space()="
            f"{self.get_xpath_text_literal(blood_type)}]]",
        )

        last_error = None

        for _ in range(5):
            try:
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

                self.click(self.BLOOD_TYPE_DROPDOWN)

                option = self.wait_for_presence(option_locator)

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    option,
                )

                self.driver.execute_script(
                    """
                    arguments[0].dispatchEvent(
                        new MouseEvent('mousedown', { bubbles: true })
                    );
                    arguments[0].dispatchEvent(
                        new MouseEvent('mouseup', { bubbles: true })
                    );
                    arguments[0].click();
                    """,
                    option,
                )

                self.wait.until(lambda _: self.get_blood_type_value() == blood_type)
                return

            except (
                StaleElementReferenceException,
                TimeoutException,
                AssertionError,
            ) as error:
                last_error = error
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

        actual_value = self.get_blood_type_value()

        raise AssertionError(
            f"Could not select Blood Type after retries. "
            f"Expected: {blood_type}, Actual: {actual_value}. "
            f"Last error: {last_error}"
        )

    def restore_blood_type_default(self, default_blood_type: str):

        if not default_blood_type:
            raise AssertionError("Default Blood Type value was not provided")

        self.update_blood_type(default_blood_type)

        self.wait.until(lambda _: self.get_blood_type_value() == default_blood_type)

        return default_blood_type

    def get_test_field_value(self):
        return self.get_attribute(self.TEST_FIELD_INPUT, "value") or ""

    def update_test_field(self, value: str):
        self.enter_text(self.TEST_FIELD_INPUT, value)

    def clear_test_field(self):
        """
        Clears Test_Field strictly and verifies blank value.
        """

        self.replace_input_value_strict(self.TEST_FIELD_INPUT, "")
        self.wait.until(lambda _: self.get_test_field_value() == "")

    def get_test_field_error_message(self):
        return self.get_text(self.TEST_FIELD_ERROR_MESSAGE)

    def is_test_field_error_displayed(self):
        return len(self.driver.find_elements(*self.TEST_FIELD_ERROR_MESSAGE)) > 0

    def save_custom_fields(self):
        self.click(self.CUSTOM_FIELDS_SAVE_BUTTON)

    def is_attachments_heading_displayed(self):
        return self.is_element_visible(self.ATTACHMENTS_HEADING)

    def is_add_attachment_button_displayed(self):
        return self.is_element_visible(self.ADD_ATTACHMENT_BUTTON)

    def highlight_attachments_heading(self):
        self.highlight_element(self.ATTACHMENTS_HEADING)

    def highlight_add_attachment_button(self):
        self.highlight_element(self.ADD_ATTACHMENT_BUTTON)

    def click_add_attachment_button(self):
        add_button = self.wait_for_clickable(self.ADD_ATTACHMENT_BUTTON)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            add_button,
        )

        self.driver.execute_script("arguments[0].click();", add_button)

    def wait_until_add_attachment_form_is_displayed(self):
        self.wait_for_visible(self.ADD_ATTACHMENT_FORM_TITLE)

    def is_add_attachment_form_displayed(self):
        return self.is_element_visible(self.ADD_ATTACHMENT_FORM_TITLE)

    def is_attachment_select_file_label_displayed(self):
        return self.is_element_visible(self.ATTACHMENT_SELECT_FILE_LABEL)

    def is_attachment_browse_button_displayed(self):
        return self.is_element_visible(self.ATTACHMENT_BROWSE_BUTTON)

    def is_attachment_comment_textarea_displayed(self):
        return self.is_element_visible(self.ATTACHMENT_COMMENT_TEXTAREA)

    def is_attachment_cancel_button_displayed(self):
        return self.is_element_visible(self.ATTACHMENT_CANCEL_BUTTON)

    def is_attachment_save_button_displayed(self):
        return self.is_element_visible(self.ATTACHMENT_SAVE_BUTTON)

    def is_attachment_file_size_hint_displayed(self):
        return self.is_element_visible(self.ATTACHMENT_FILE_SIZE_HINT)

    def highlight_add_attachment_form_title(self):
        self.highlight_element(self.ADD_ATTACHMENT_FORM_TITLE)

    def highlight_attachment_browse_button(self):
        self.highlight_element(self.ATTACHMENT_BROWSE_BUTTON)

    def highlight_attachment_comment_textarea(self):
        self.highlight_element(self.ATTACHMENT_COMMENT_TEXTAREA)

    def highlight_attachment_save_button(self):
        self.highlight_element(self.ATTACHMENT_SAVE_BUTTON)

    def highlight_attachment_cancel_button(self):
        self.highlight_element(self.ATTACHMENT_CANCEL_BUTTON)

    def get_attachment_file_required_error_message(self):
        return self.get_text(self.ATTACHMENT_FILE_REQUIRED_ERROR_MESSAGE)

    def highlight_attachment_file_required_error_message(self):
        self.highlight_element(self.ATTACHMENT_FILE_REQUIRED_ERROR_MESSAGE)

    def save_attachment(self):
        self.click(self.ATTACHMENT_SAVE_BUTTON)

    def enter_attachment_comment(self, comment: str):
        self.enter_text(self.ATTACHMENT_COMMENT_TEXTAREA, comment)

    def get_attachment_comment_error_message(self):
        return self.get_text(self.ATTACHMENT_COMMENT_ERROR_MESSAGE)

    def highlight_attachment_comment_error_message(self):
        self.highlight_element(self.ATTACHMENT_COMMENT_ERROR_MESSAGE)

    def upload_attachment_file(self, file_path: str):
        self.wait_for_presence(self.ATTACHMENT_FILE_INPUT).send_keys(file_path)

    def is_attachment_file_displayed(self, file_name: str):
        attachment_file_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            f"//div[contains(@class,'oxd-table-card')]"
            f"//div[contains(normalize-space(), {self.get_xpath_text_literal(file_name)})]",
        )

        return self.is_element_visible(attachment_file_locator)

    def highlight_uploaded_attachment_file(self, file_name: str):
        attachment_file_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            f"//div[contains(@class,'oxd-table-card')]"
            f"//div[contains(normalize-space(), {self.get_xpath_text_literal(file_name)})]",
        )

        self.highlight_element(attachment_file_locator)

    def wait_until_attachment_file_is_displayed(self, file_name: str):
        attachment_file_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            "//div[contains(@class,'oxd-table-card')]"
            f"//div[contains(normalize-space(), {self.get_xpath_text_literal(file_name)})]",
        )

        self.wait.until(lambda _: self.is_element_visible(attachment_file_locator))

    def get_attachment_row_by_file_name(self, file_name: str):
        attachment_row_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            "//div[contains(@class,'oxd-table-card')]"
            f"[.//div[contains(normalize-space(), {self.get_xpath_text_literal(file_name)})]]",
        )

        return self.wait_for_visible(attachment_row_locator)

    def click_edit_attachment_by_file_name(self, file_name: str):
        attachment_row = self.get_attachment_row_by_file_name(file_name)

        edit_button = attachment_row.find_element(
            By.XPATH,
            ".//button[.//i[contains(@class,'bi-pencil-fill')]]",
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            edit_button,
        )

        self.driver.execute_script("arguments[0].click();", edit_button)

    def is_edit_attachment_form_displayed(self):
        return self.is_element_visible(self.EDIT_ATTACHMENT_FORM_TITLE)

    def highlight_edit_attachment_form_title(self):
        self.highlight_element(self.EDIT_ATTACHMENT_FORM_TITLE)

    def get_edit_attachment_current_file_name(self):
        elements = self.driver.find_elements(*self.EDIT_ATTACHMENT_CURRENT_FILE_TEXT)

        if not elements:
            return ""

        return elements[0].text.strip()

    def get_edit_attachment_selected_file_name(self):
        return self.get_text(self.EDIT_ATTACHMENT_SELECTED_FILE_TEXT)

    def replace_attachment_file(self, file_path: str):
        file_input = self.wait_for_presence(self.EDIT_ATTACHMENT_REPLACE_FILE_INPUT)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            file_input,
        )

        file_input.send_keys(file_path)

    def wait_until_edit_attachment_selected_file_is(self, file_name: str):
        self.wait.until(
            lambda _: file_name in self.get_edit_attachment_selected_file_name()
        )

    def replace_attachment_comment(self, comment: str):
        self.wait_until_attachment_form_loader_disappears()

        comment_field = self.wait_for_visible(self.ATTACHMENT_COMMENT_TEXTAREA)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            comment_field,
        )

        self.wait_until_attachment_form_loader_disappears()

        self.driver.execute_script(
            """
            const textarea = arguments[0];
            const value = arguments[1];

            const nativeTextAreaValueSetter =
                Object.getOwnPropertyDescriptor(
                    window.HTMLTextAreaElement.prototype,
                    'value'
                ).set;

            nativeTextAreaValueSetter.call(textarea, '');
            textarea.dispatchEvent(new Event('input', { bubbles: true }));
            textarea.dispatchEvent(new Event('change', { bubbles: true }));

            nativeTextAreaValueSetter.call(textarea, value);
            textarea.dispatchEvent(new Event('input', { bubbles: true }));
            textarea.dispatchEvent(new Event('change', { bubbles: true }));
            textarea.dispatchEvent(new Event('blur', { bubbles: true }));
            """,
            comment_field,
            comment,
        )

        self.wait.until(lambda _: self.get_attachment_comment_value() == comment)

    def wait_until_attachment_file_input_contains(self, file_name: str):
        self.wait.until(
            lambda _: file_name
            in (self.get_attribute(self.ATTACHMENT_FILE_INPUT, "value") or "")
        )

    def save_edited_attachment(self):
        self.click(self.EDIT_ATTACHMENT_SAVE_BUTTON)

    def is_attachment_comment_displayed(self, comment: str):
        attachment_comment_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            "//div[contains(@class,'oxd-table-card')]"
            f"//div[contains(normalize-space(), {self.get_xpath_text_literal(comment)})]",
        )

        return self.is_element_visible(attachment_comment_locator)

    def wait_until_attachment_comment_is_displayed(self, comment: str):
        attachment_comment_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            "//div[contains(@class,'oxd-table-card')]"
            f"//div[contains(normalize-space(), {self.get_xpath_text_literal(comment)})]",
        )

        self.wait.until(lambda _: self.is_element_visible(attachment_comment_locator))

    def highlight_uploaded_attachment_comment(self, comment: str):
        attachment_comment_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            "//div[contains(@class,'oxd-table-card')]"
            f"//div[contains(normalize-space(), {self.get_xpath_text_literal(comment)})]",
        )

        self.highlight_element(attachment_comment_locator)

    def click_delete_attachment_by_file_name(self, file_name: str):
        attachment_row = self.get_attachment_row_by_file_name(file_name)

        delete_button = attachment_row.find_element(
            By.XPATH,
            ".//button[.//i[contains(@class,'bi-trash')]]",
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            delete_button,
        )

        self.driver.execute_script("arguments[0].click();", delete_button)

    def highlight_delete_attachment_button_by_file_name(self, file_name: str):
        attachment_row = self.get_attachment_row_by_file_name(file_name)

        delete_button = attachment_row.find_element(
            By.XPATH,
            ".//button[.//i[contains(@class,'bi-trash')]]",
        )

        self.driver.execute_script(
            "arguments[0].style.border = '4px solid red';"
            "arguments[0].style.boxShadow = '0 0 10px red';",
            delete_button,
        )

    def is_delete_attachment_confirmation_modal_displayed(self):
        return self.is_element_visible(self.DELETE_ATTACHMENT_CONFIRMATION_MODAL)

    def highlight_delete_attachment_confirmation_modal(self):
        self.highlight_element(self.DELETE_ATTACHMENT_CONFIRMATION_MODAL)

    def confirm_delete_attachment(self):
        self.click(self.CONFIRM_DELETE_ATTACHMENT_BUTTON)

    def wait_until_attachment_file_is_removed(self, file_name: str):
        attachment_file_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            "//div[contains(@class,'oxd-table-card')]"
            f"//div[contains(normalize-space(), {self.get_xpath_text_literal(file_name)})]",
        )

        self.wait.until(
            lambda _: len(self.driver.find_elements(*attachment_file_locator)) == 0
        )

    def get_attachment_comment_value(self):
        return self.get_attribute(self.ATTACHMENT_COMMENT_TEXTAREA, "value") or ""

    def is_attachment_row_displayed_by_file_name_and_comment(
        self, file_name: str, comment: str
    ):
        attachment_row_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            "//div[contains(@class,'oxd-table-card')]"
            f"[.//div[contains(normalize-space(), {self.get_xpath_text_literal(file_name)})]"
            f" and .//div[contains(normalize-space(), {self.get_xpath_text_literal(comment)})]]",
        )

        return self.is_element_visible(attachment_row_locator)

    def wait_until_attachment_row_is_displayed_by_file_name_and_comment(
        self, file_name: str, comment: str
    ):
        attachment_row_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            "//div[contains(@class,'oxd-table-card')]"
            f"[.//div[contains(normalize-space(), {self.get_xpath_text_literal(file_name)})]"
            f" and .//div[contains(normalize-space(), {self.get_xpath_text_literal(comment)})]]",
        )

        self.wait.until(lambda _: self.is_element_visible(attachment_row_locator))

    def highlight_attachment_row_by_file_name_and_comment(
        self, file_name: str, comment: str
    ):
        attachment_row_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            "//div[contains(@class,'oxd-table-card')]"
            f"[.//div[contains(normalize-space(), {self.get_xpath_text_literal(file_name)})]"
            f" and .//div[contains(normalize-space(), {self.get_xpath_text_literal(comment)})]]",
        )

        self.highlight_element(attachment_row_locator)

    def click_edit_attachment_by_file_name_and_comment(
        self, file_name: str, comment: str
    ):
        attachment_row = self.get_attachment_row_by_file_name_and_comment(
            file_name,
            comment,
        )

        edit_button = attachment_row.find_element(
            By.XPATH,
            ".//button[.//i[contains(@class,'bi-pencil-fill')]]",
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            edit_button,
        )

        self.driver.execute_script("arguments[0].click();", edit_button)

    def get_attachment_row_by_file_name_and_comment(self, file_name: str, comment: str):
        attachment_row_locator = (
            By.XPATH,
            "//h6[normalize-space()='Attachments']"
            "/following::div[contains(@class,'oxd-table-body')][1]"
            "//div[contains(@class,'oxd-table-card')]"
            f"[.//div[contains(normalize-space(), {self.get_xpath_text_literal(file_name)})]"
            f" and .//div[contains(normalize-space(), {self.get_xpath_text_literal(comment)})]]",
        )

        return self.wait_for_visible(attachment_row_locator)

    def wait_until_attachment_form_loader_disappears(self):
        self.wait.until(
            lambda _: len(self.driver.find_elements(*self.ATTACHMENT_FORM_LOADER)) == 0
        )

    def get_all_attachment_rows_text(self):
        rows = self.driver.find_elements(*self.ATTACHMENT_TABLE_ROWS)
        return [row.text for row in rows]

    def wait_until_edit_attachment_current_file_is(self, expected_file_name: str):
        self.wait.until(
            lambda _: expected_file_name
            in (self.get_edit_attachment_current_file_name() or "")
        )
