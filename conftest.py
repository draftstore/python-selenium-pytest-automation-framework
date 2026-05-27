import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader


@pytest.fixture
def driver():
    """
    Creates a browser instance before each test
    and closes it automatically after the test.
    """

    browser = ConfigReader.get_browser()
    headless = ConfigReader.is_headless()

    if browser.lower() == "chrome":
        options = Options()
        options.add_argument("--start-maximized")

        if headless:
            options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(0)
    
    yield driver
    
    final_pause = ConfigReader.get_final_pause()
    
    if final_pause > 0:
        time.sleep(final_pause)
        driver.quit()