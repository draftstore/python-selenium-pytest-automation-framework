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
