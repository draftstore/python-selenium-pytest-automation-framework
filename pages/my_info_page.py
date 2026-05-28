from selenium.webdriver.common.by import By

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

    # ID Section
    EMPLOYEE_ID_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Employee Id']"
        "/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    OTHER_ID_INPUT = (
    By.XPATH,
    "//label[normalize-space()='Other Id']"
    "/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )
    
    DRIVERS_LICENSE_INPUT = (
    By.XPATH,
    "//label[normalize-space()=\"Driver's License Number\"]"
    "/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    LICENSE_EXPIRY_DATE_INPUT = (
        By.XPATH,
        "//label[normalize-space()='License Expiry Date']"
        "/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    # Personal Information Section
    NATIONALITY_DROPDOWN = (
        By.XPATH,
        "//label[normalize-space()='Nationality']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]"
    )

    MARITAL_STATUS_DROPDOWN = (
        By.XPATH,
        "//label[normalize-space()='Marital Status']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]"
    )

    DATE_OF_BIRTH_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Date of Birth']"
        "/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )
    
    MALE_RADIO_INPUT = (
    By.XPATH,
    "//label[normalize-space()='Male']//input[@type='radio']"
    )
    
    FEMALE_RADIO_INPUT = (
    By.XPATH,
    "//label[normalize-space()='Female']//input[@type='radio']"
    )
    
    MALE_RADIO_CLICK_TARGET = (
    By.XPATH,
    "//label[normalize-space()='Male']//span[contains(@class,'oxd-radio-input')]"
    )
    
    FEMALE_RADIO_CLICK_TARGET = (
    By.XPATH,
    "//label[normalize-space()='Female']//span[contains(@class,'oxd-radio-input')]"
    )
    
    # Save Button
    PERSONAL_DETAILS_SAVE_BUTTON = (By.XPATH,
    "//label[normalize-space()='Marital Status']"
    "/ancestor::form//button[@type='submit' and normalize-space()='Save']"
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
        success_message = (
            By.XPATH,
            "//p[normalize-space()='Successfully Updated']"
        )
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
        if self.is_custom_dropdown_option_available(self.NATIONALITY_DROPDOWN, original_value):
            self.update_nationality(original_value)
            return True
        return False
        
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
        if self.is_custom_dropdown_option_available(self.MARITAL_STATUS_DROPDOWN, original_value):
            self.update_marital_status(original_value)
            return True
        return False