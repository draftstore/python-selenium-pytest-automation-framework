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
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='First Name']")
    MIDDLE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Middle Name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='Last Name']")

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
        "//label[contains(normalize-space(), \"Driver's License\")]"
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

    MALE_RADIO_LABEL = (By.XPATH, "//label[normalize-space()='Male']")
    FEMALE_RADIO_LABEL = (By.XPATH, "//label[normalize-space()='Female']")

    # Save Button
    PERSONAL_DETAILS_SAVE_BUTTON = (
        By.XPATH,
        "(//button[@type='submit' and normalize-space()='Save'])[1]"
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
            self.is_element_visible(self.FIRST_NAME_INPUT)
            and self.is_element_visible(self.MIDDLE_NAME_INPUT)
            and self.is_element_visible(self.LAST_NAME_INPUT)
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
            and self.is_element_visible(self.MALE_RADIO_LABEL)
            and self.is_element_visible(self.FEMALE_RADIO_LABEL)
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