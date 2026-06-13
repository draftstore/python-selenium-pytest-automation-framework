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


_FAILED_TESTS = []


def _get_clean_failure_reason(call):
    if not call.excinfo:
        return "Unknown error"

    exception_type = call.excinfo.type.__name__
    exception_value = call.excinfo.value

    raw_message = getattr(exception_value, "msg", None) or str(exception_value)
    raw_message = raw_message.strip()

    if "Stacktrace:" in raw_message:
        raw_message = raw_message.split("Stacktrace:")[0].strip()

    message_lines = [
        line.strip()
        for line in raw_message.splitlines()
        if line.strip() and line.strip().lower() not in ["message:", "stacktrace:"]
    ]

    if message_lines:
        clean_message = message_lines[0]
    else:
        clean_message = "No detailed error message provided"

    return f"{exception_type}: {clean_message}"


def _get_clean_failure_location(item, call, report):
    test_name = report.location[2]
    file_path = report.location[0]
    line_number = report.location[1] + 1

    if not call.excinfo:
        return test_name, file_path, line_number

    project_root = Path(str(item.config.rootpath)).resolve()

    project_traceback_entries = []

    for entry in call.excinfo.traceback:
        entry_path = Path(str(entry.path)).resolve()
        entry_path_text = str(entry_path).lower()

        is_external_file = (
            "site-packages" in entry_path_text or "venv" in entry_path_text
        )

        is_project_file = (
            entry_path == project_root or project_root in entry_path.parents
        )

        if is_project_file and not is_external_file:
            project_traceback_entries.append(entry)

    if project_traceback_entries:
        failed_entry = project_traceback_entries[-1]
        failed_path = Path(str(failed_entry.path)).resolve()

        try:
            file_path = str(failed_path.relative_to(project_root))
        except ValueError:
            file_path = str(failed_path)

        line_number = failed_entry.lineno + 1

    return test_name, file_path, line_number


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    if not report.failed:
        return

    test_name, file_path, line_number = _get_clean_failure_location(
        item,
        call,
        report,
    )

    reason = _get_clean_failure_reason(call)

    _FAILED_TESTS.append(
        {
            "test": test_name,
            "file": file_path,
            "line": line_number,
            "reason": reason,
        }
    )


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if not _FAILED_TESTS:
        return

    terminalreporter.write_line("")
    terminalreporter.write_line("========== CLEAN FAILURE SUMMARY ==========")

    for failed_test in _FAILED_TESTS:
        terminalreporter.write_line("[FAILED]")
        terminalreporter.write_line(f"Test  : {failed_test['test']}")
        terminalreporter.write_line(f"File  : {failed_test['file']}")
        terminalreporter.write_line(f"Line  : {failed_test['line']}")
        terminalreporter.write_line(f"Reason: {failed_test['reason']}")
        terminalreporter.write_line("------------------------------------------")

    terminalreporter.write_line("===========================================")
