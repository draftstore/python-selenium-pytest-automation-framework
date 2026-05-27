# Python Selenium Pytest Automation Framework - Learning Log

এই document-এ আমি আমার Selenium Automation Framework project-এর প্রতিটি important step note করে রাখছি, যাতে পরবর্তীতে project review করলে সহজে বুঝতে পারি কোন step কেন করা হয়েছিল।

---

## Project Goal

এই project-এর মূল উদ্দেশ্য হলো Python, Selenium, Pytest এবং Page Object Model ব্যবহার করে একটি professional automation testing framework তৈরি করা।

এই project-এর মাধ্যমে আমি দেখাতে চাই:

- Python programming fundamentals
- Selenium WebDriver automation
- Pytest test framework usage
- Page Object Model design pattern
- Reusable automation methods
- Clean project structure
- Test validation and reporting
- Real-world SQA automation workflow

---

## Repository Setup

1. GitHub repository তৈরি করা হয়েছে: python-selenium-pytest-automation-framework
2. Repository purpose: A production-style Selenium automation framework built with Python and Pytest, focused on real-world QA automation practices.
3. Initial setup includes:

- README.md
- Python .gitignore
- MIT License
- Virtual environment
- requirements.txt
- Project folders

## Project Folder Structure

python-selenium-pytest-automation-framework/
│
├── config/
│ └── config.json
│
├── docs/
│ └── project-learning-log-bn.md
│
├── pages/
│ ├── base_page.py
│ ├── login_page.py
│ ├── dashboard_page.py
│ └── my_info_page.py
│
├── tests/
│ ├── test_login.py
│ └── test_my_info_personal_details.py
│
├── utils/
│ ├── config_reader.py
│ ├── logger.py
│ └── screenshot.py
│
├── reports/
├── screenshots/
├── logs/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

Environment Setup

Virtual environment create করা হয়েছে:

- python -m venv venv

Virtual environment activate করা হয়েছে:

- .\venv\Scripts\Activate.ps1

## Required packages install করা হয়েছে:

pip install selenium pytest pytest-html webdriver-manager

## Installed packages save করা হয়েছে:

- pip freeze > requirements.txt
- Git Ignore Setup
- .gitignore file configure করা হয়েছে যাতে generated files GitHub-এ push না হয়।

## Ignored items:

venv/
**pycache**/
.pytest*cache/
reports/*
screenshots/\_
logs/\*

কিন্তু folder structure রাখার জন্য .gitkeep ব্যবহার করা হয়েছে:

reports/.gitkeep
screenshots/.gitkeep
logs/.gitkeep
Pytest Configuration

## pytest.ini file configure করা হয়েছে:

- [pytest]
- testpaths = tests
- python*files = test*\*.py
- python*functions = test*\*
- addopts = -v --html=reports/report.html --self-contained-html
- এর মাধ্যমে test run করলে automatic HTML report generate হয়: reports/report.html

## Config File Setup

config/config.json file - তৈরি করা হয়েছে project settings manage করার জন্য।
{
"base_url": "https://opensource-demo.orangehrmlive.com/",
"browser": "chrome",
"timeout": 10,
"headless": false,
"slow_mode": 1,
"final_pause": 5
}

এই config file ব্যবহার করার কারণ:

- URL hardcode না করা
- Browser setting central place থেকে control করা
- Timeout reusable রাখা
- Slow mode/debug mode control করা
- Final browser pause control করা
- Config Reader Utility

## utils/config_reader.py তৈরি করা হয়েছে config.json থেকে settings read করার জন্য।

এই file-এর মাধ্যমে project-এ Python concepts ব্যবহার করা হয়েছে:

Class
Static methods
JSON handling
File path handling
Reusable utility design
Browser Fixture Setup

## conftest.py file-এ Pytest fixture তৈরি করা হয়েছে।

Purpose:

- Browser open করা
- Config থেকে browser/headless setting নেওয়া
- Test execute করা
- Final pause apply করা
- Test শেষে browser close করা

Professional reason: Test file-এর ভিতরে বারবার webdriver.Chrome() লেখা হয়নি। Browser setup central fixture দিয়ে manage করা হয়েছে।

## BasePage Created

pages/base_page.py তৈরি করা হয়েছে reusable Selenium actions রাখার জন্য।

BasePage includes:

- Browser actions
- Explicit waits
- Element actions
- Keyboard actions
- Mouse actions
- JavaScript actions
- Dropdown handling
- Checkbox/radio handling
- Alert handling
- Frame handling
- Window/tab handling
- Screenshot method

Purpose: Page classes যেন clean থাকে এবং repeated Selenium code না লিখতে হয়।
For an example:

- self.click(locator)
- self.enter_text(locator, text)
- self.get_text(locator)
- self.hover(locator)
- Login Page Automation

## pages/login_page.py তৈরি করা হয়েছে OrangeHRM Login page-এর জন্য।

Covered locators:

- Username input
- Password input
- Login button
- Error message

Login method: login_page.login("Admin", "admin123")

Important learning:Username/password login_page.py-এর ভিতরে hardcode করা হয়নি। Test file থেকে parameter হিসেবে পাঠানো হয়েছে।

## Dashboard Page Object

pages/dashboard_page.py তৈরি করা হয়েছে successful login validate করার জন্য।

Covered:

- Dashboard header
- User dropdown
- Logout link

## Main validation:

- dashboard_page.is_dashboard_displayed()
- Login Test

## tests/test_login.py তৈরি করা হয়েছে valid login flow verify করার জন্য।

Test flow:

- Open OrangeHRM login page
- Enter valid username and password
- Click Login
- Verify Dashboard page is displayed

# Run command: python -m pytest tests/test_login.py -v

Expected result:
============== 1 passed ==================

## My Info Personal Details Page Object

pages/my_info_page.py তৈরি করা হয়েছে My Info → Personal Details page automation-এর জন্য।

Flow:

- Login
- Dashboard
- Click My Info sidebar
- Open Personal Details page

## Covered fields:

- Name Section
- First Name
- Middle Name
- Last Name
- ID Section
- Employee ID
- Other ID
- Driver’s License Number
- License Expiry Date
- Personal Information Section
- Nationality dropdown
- Marital Status dropdown
- Date of Birth
- Gender radio buttons
- Action
- Save button

Locator strategy: Absolute XPath ব্যবহার করা হয়নি। Label-based XPath ব্যবহার করা হয়েছে যাতে locator stable এবং readable থাকে।

Example: "//label[normalize-space()='Employee Id']/ancestor::div[contains(@class,'oxd-input-group')]//input"

## Personal Details Smoke Test

tests/test_my_info_personal_details.py তৈরি করা হয়েছে Personal Details page smoke validation করার জন্য।

Test flow:

- Login with valid credentials
- Verify Dashboard page
- Click My Info
- Verify Personal Details page
- Verify name fields are visible
- Verify ID fields are visible
- Verify personal information fields are visible
- Verify First Name is pre-filled
- Verify Last Name is pre-filled
- Verify Save button is visible

## Run command: python -m pytest tests/test_my_info_personal_details.py -v

Expected result:
============== 1 passed ==================

Important SQA Learning
প্রথমে Employee ID auto-populated হবে ধরে assertion লেখা হয়েছিল। কিন্তু test fail করার পর বুঝা যায় OrangeHRM demo data অনুযায়ী Employee ID blank থাকতে পারে। তাই assertion update করা হয়েছে।

Old assumption:
Employee ID must not be empty

Corrected validation:
Employee ID field must be visible
First Name and Last Name should be pre-filled

## Current Completed Milestones:

- GitHub repository setup
- Virtual environment setup
- Python project structure
- Pytest configuration
- JSON-based config management
- Browser fixture setup
- Reusable BasePage
- OrangeHRM Login Page Object
- Dashboard Page Object
- Valid login test
- My Info Personal Details Page Object
- Personal Details smoke validation
- HTML report generation
- Test Commands Used

## Run login test: python -m pytest tests/test_login.py -v

## Run Personal Details smoke test: python -m pytest tests/test_my_info_personal_details.py -v

## Run all tests: python -m pytest -v

## Generated report location: reports/report.html
