import json
import platform
import time
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import ConfigReader


ALLURE_RESULTS_DIR = Path("reports") / "allure-results"


def pytest_sessionstart(session):
    """
    Creates Allure environment and executor metadata before test execution.
    This helps make the Allure report more informative and professional.
    """

    ALLURE_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    environment_data = {
        "Application": "OrangeHRM Demo",
        "Base_URL": ConfigReader.get_base_url(),
        "Environment": "Demo",
        "Browser": ConfigReader.get_browser().capitalize(),
        "Headless_Mode": str(ConfigReader.is_headless()),
        "Automation_Tool": "Selenium WebDriver",
        "Test_Framework": "Pytest",
        "Reporting_Tool": "Allure Report",
        "Programming_Language": "Python",
        "Design_Pattern": "Page Object Model",
        "Tester": "Md Al Amin Siam",
        "Operating_System": platform.system(),
        "OS_Version": platform.version(),
        "Python_Version": platform.python_version(),
    }

    environment_file = ALLURE_RESULTS_DIR / "environment.properties"

    with open(environment_file, "w", encoding="utf-8") as file:
        for key, value in environment_data.items():
            file.write(f"{key}={value}\n")

    executor_data = {
        "name": "Local Machine",
        "type": "local",
        "buildName": "Selenium Pytest Automation Framework",
        "reportName": "OrangeHRM Automation Test Report",
    }

    executor_file = ALLURE_RESULTS_DIR / "executor.json"

    with open(executor_file, "w", encoding="utf-8") as file:
        json.dump(executor_data, file, indent=4)


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