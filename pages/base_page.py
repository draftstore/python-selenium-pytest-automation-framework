from typing import Tuple, List
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from utils.config_reader import ConfigReader

Locator = Tuple[By, str]

class BasePage:
    """
    BasePage contains reusable Selenium WebDriver actions.

    This class is designed to keep page classes clean and readable.
    All page object classes should inherit from BasePage.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, ConfigReader.get_timeout())
        self.slow_mode = ConfigReader.get_slow_mode()

    # -------------------------
    # Browser Actions
    # -------------------------

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def get_page_title(self) -> str:
        return self.driver.title

    def get_current_url(self) -> str:
        return self.driver.current_url

    def refresh_page(self) -> None:
        self.driver.refresh()

    def go_back(self) -> None:
        self.driver.back()

    def go_forward(self) -> None:
        self.driver.forward()

    # -------------------------
    # Wait Methods
    # -------------------------

    def wait_for_visible(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_invisible(self, locator: Locator) -> bool:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_url_contains(self, expected_text: str) -> bool:
        return self.wait.until(EC.url_contains(expected_text))

    def wait_for_title_contains(self, expected_text: str) -> bool:
        return self.wait.until(EC.title_contains(expected_text))

    def wait_for_element_count_to_be_more_than(
        self, locator: Locator, count: int
    ) -> bool:
        return self.wait.until(
            lambda driver: len(driver.find_elements(*locator)) > count
        )

    # -------------------------
    # Find Element Methods
    # -------------------------

    def find_element(self, locator: Locator) -> WebElement:
        return self.wait_for_presence(locator)

    def find_elements(self, locator: Locator) -> List[WebElement]:
        return self.driver.find_elements(*locator)

    # -------------------------
    # Basic Element Actions
    # -------------------------
    def click(self, locator: Locator) -> None:
        element = self.wait_for_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.pause_for_demo()
        element.click()
        
    def enter_text(self, locator: Locator, text: str) -> None:
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.pause_for_demo()
        element.click()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)

    def clear_text(self, locator: Locator) -> None:
        element = self.wait_for_visible(locator)
        element.clear()

    def get_text(self, locator: Locator) -> str:
        element = self.wait_for_visible(locator)
        return element.text

    def get_attribute(self, locator: Locator, attribute_name: str) -> str:
        element = self.wait_for_presence(locator)
        return element.get_attribute(attribute_name)

    def get_css_value(self, locator: Locator, property_name: str) -> str:
        element = self.wait_for_presence(locator)
        return element.value_of_css_property(property_name)

    # -------------------------
    # Element State Checks
    # -------------------------

    def is_element_visible(self, locator: Locator) -> bool:
        try:
            return self.wait_for_visible(locator).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def is_element_enabled(self, locator: Locator) -> bool:
        try:
            return self.wait_for_presence(locator).is_enabled()
        except (TimeoutException, NoSuchElementException):
            return False

    def is_element_selected(self, locator: Locator) -> bool:
        try:
            return self.wait_for_presence(locator).is_selected()
        except (TimeoutException, NoSuchElementException):
            return False

    # -------------------------
    # Keyboard Actions
    # -------------------------

    def press_enter(self, locator: Locator) -> None:
        element = self.wait_for_visible(locator)
        element.send_keys(Keys.ENTER)

    def press_tab(self, locator: Locator) -> None:
        element = self.wait_for_visible(locator)
        element.send_keys(Keys.TAB)

    def press_escape(self, locator: Locator) -> None:
        element = self.wait_for_visible(locator)
        element.send_keys(Keys.ESCAPE)

    # -------------------------
    # Mouse Actions
    # -------------------------

    def hover(self, locator: Locator) -> None:
        element = self.wait_for_visible(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def hover_and_click(self, hover_locator: Locator, click_locator: Locator) -> None:
        self.hover(hover_locator)
        element = self.wait_for_clickable(click_locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def double_click(self, locator: Locator) -> None:
        element = self.wait_for_clickable(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator: Locator) -> None:
        element = self.wait_for_clickable(locator)
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, source_locator: Locator, target_locator: Locator) -> None:
        source = self.wait_for_visible(source_locator)
        target = self.wait_for_visible(target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    # -------------------------
    # JavaScript Actions
    # -------------------------
    
    def scroll_to_element(self, locator: Locator) -> None:
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def scroll_to_top(self) -> None:
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def js_click(self, locator: Locator) -> None:
        element = self.wait_for_presence(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def js_enter_text(self, locator: Locator, text: str) -> None:
        element = self.wait_for_presence(locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, text)

    def highlight_element(self, locator: Locator) -> None:
        element = self.wait_for_visible(locator)
        self.driver.execute_script(
            "arguments[0].style.border='3px solid red';", element
        )

    # -------------------------
    # Dropdown Actions
    # -------------------------

    def select_dropdown_by_visible_text(self, locator: Locator, text: str) -> None:
        element = self.wait_for_visible(locator)
        Select(element).select_by_visible_text(text)

    def select_dropdown_by_value(self, locator: Locator, value: str) -> None:
        element = self.wait_for_visible(locator)
        Select(element).select_by_value(value)

    def select_dropdown_by_index(self, locator: Locator, index: int) -> None:
        element = self.wait_for_visible(locator)
        Select(element).select_by_index(index)

    def get_selected_dropdown_text(self, locator: Locator) -> str:
        element = self.wait_for_visible(locator)
        return Select(element).first_selected_option.text

    def get_all_dropdown_options(self, locator: Locator) -> List[str]:
        element = self.wait_for_visible(locator)
        return [option.text for option in Select(element).options]

    # -------------------------
    # Checkbox / Radio Button Actions
    # -------------------------

    def select_checkbox(self, locator: Locator) -> None:
        element = self.wait_for_clickable(locator)
        if not element.is_selected():
            element.click()

    def unselect_checkbox(self, locator: Locator) -> None:
        element = self.wait_for_clickable(locator)
        if element.is_selected():
            element.click()

    def select_radio_button(self, locator: Locator) -> None:
        element = self.wait_for_clickable(locator)
        if not element.is_selected():
            element.click()

    # -------------------------
    # Alert Actions
    # -------------------------

    def accept_alert(self) -> None:
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def dismiss_alert(self) -> None:
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()

    def get_alert_text(self) -> str:
        alert = self.wait.until(EC.alert_is_present())
        return alert.text

    def enter_text_in_alert(self, text: str) -> None:
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)

    # -------------------------
    # Frame Actions
    # -------------------------

    def switch_to_frame_by_locator(self, locator: Locator) -> None:
        frame = self.wait_for_presence(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_frame_by_index(self, index: int) -> None:
        self.driver.switch_to.frame(index)

    def switch_to_frame_by_name_or_id(self, name_or_id: str) -> None:
        self.driver.switch_to.frame(name_or_id)

    def switch_to_default_content(self) -> None:
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self) -> None:
        self.driver.switch_to.parent_frame()

    # -------------------------
    # Window / Tab Actions
    # -------------------------

    def get_current_window_handle(self) -> str:
        return self.driver.current_window_handle

    def get_all_window_handles(self) -> List[str]:
        return self.driver.window_handles

    def switch_to_window_by_index(self, index: int) -> None:
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])

    def switch_to_new_window(self) -> None:
        current_window = self.driver.current_window_handle
        self.wait.until(lambda driver: len(driver.window_handles) > 1)

        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break

    def close_current_window(self) -> None:
        self.driver.close()

    # -------------------------
    # Screenshot
    # -------------------------

    def take_screenshot(self, file_path: str) -> None:
        self.driver.save_screenshot(file_path)

    # -------------------------
    # Pause for Demo
    # -------------------------
    def pause_for_demo(self):
        if self.slow_mode > 0:
            time.sleep(self.slow_mode)
            
    def select_custom_dropdown_option(self, dropdown_locator: Locator, option_text: str) -> None:
        self.click(dropdown_locator)
        option_locator = (By.XPATH,f"//div[@role='option']//span[normalize-space()='{option_text}']")
        self.click(option_locator)

    def get_custom_dropdown_selected_text(self, dropdown_locator: Locator) -> str:
        return self.get_text(dropdown_locator).strip()