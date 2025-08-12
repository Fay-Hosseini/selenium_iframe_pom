Sure! Here’s a detailed `README.md` file tailored to your Selenium iframe project, incorporating all the troubleshooting tips, usage instructions, and best practices we covered:

---

# Selenium Iframe Handling with Pytest

This project demonstrates how to interact with iframes using Selenium WebDriver in Python with a Pytest test framework, including best practices, troubleshooting tips, and examples.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Setup & Installation](#setup--installation)
* [Project Structure](#project-structure)
* [Key Features](#key-features)
* [Usage Instructions](#usage-instructions)
* [Troubleshooting & Common Issues](#troubleshooting--common-issues)
* [Keeping Browser Open After Tests](#keeping-browser-open-after-tests)
* [Contributing](#contributing)
* [License](#license)

---

## Project Overview

This project uses the Page Object Model (POM) to structure Selenium tests that interact with multiple iframes on a web page. It includes:

* Identifying and printing all iframes on a page.
* Switching to iframes and interacting with elements inside.
* Waiting for elements using explicit waits.
* Proper locator strategies for iframe and internal elements.
* Tips on maximizing browser window and controlling browser lifecycle.

---

## Setup & Installation

1. **Clone the repo** (or download source):

   ```bash
   git clone <repository-url>
   cd selenium_iframe_pom
   ```

2. **Create a Python virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

   *(Make sure `selenium` and `pytest` are installed)*

4. **Download ChromeDriver** matching your Chrome version from:

   [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

   Add it to your system PATH or specify the executable path in the fixture.

---

## Project Structure

```
selenium_iframe_pom/
│
├── pages/
│   └── iframe_page.py          # Page Object class for iframe interactions
│   └── base_page.py            # BasePage with common functionality
│
├── tests/
│   └── test_iframe.py          # Pytest test cases
│
├── conftest.py                 # Pytest fixtures for WebDriver setup
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## Key Features

* **Detect and list all iframes on a page.**
* **Switch to a specific iframe by ID and interact with internal elements.**
* **Explicit waits to handle dynamic page loads and iframe availability.**
* **Page maximization via WebDriver options.**
* **Option to keep browser open after test run for debugging.**

---

## Usage Instructions

1. **Run tests with Pytest:**

   ```bash
   pytest tests/test_iframe.py
   ```

2. **Sample test usage (from `test_iframe.py`):**

   ```python
   from pages.iframe_page import IframePage

   def test_internal_button_click(driver):
       page = IframePage(driver)
       page.load()
       page.subscribe_inner_iframe("test@example.com")
   ```

3. **Maximizing the browser:**

   The browser window is maximized inside the `driver` fixture in `conftest.py`.

4. **Locators:**

   * Ensure iframe locators (e.g., by ID) are correct by inspecting the page source.
   * Ensure elements inside the iframe use correct locators (e.g., `email` input inside iframe has id `email`).

---

## Troubleshooting & Common Issues

### 1. **TimeoutException when waiting for elements inside iframe**

* Confirm you have switched to the correct iframe before locating elements.
* Verify the iframe locator and element locator using browser devtools.
* Use explicit waits for iframe availability:

  ```python
  wait.until(EC.frame_to_be_available_and_switch_to_it(IFRAME_LOCATOR))
  ```

### 2. **Page source inside iframe not as expected**

* Use `print(driver.page_source)` right after switching to iframe to debug current HTML.

### 3. **Iframe locators**

* Use valid locators. Example:

  ```python
  VIDEO_IFRAME = (By.ID, "iframe-youtube")
  # or XPath:
  VIDEO_IFRAME = (By.XPATH, '//iframe[@id="iframe-youtube"]')
  ```

### 4. **Browser closes immediately after test**

* Pytest tears down the fixture after tests by default.
* To keep browser open for debugging, add a `input()` or `time.sleep()` after yielding driver in the fixture:

  ```python
  @pytest.fixture(scope="session")
  def driver():
      driver = webdriver.Chrome()
      driver.maximize_window()
      yield driver
      input("Press Enter to close browser...")
      driver.quit()
  ```

---

## Keeping Browser Open After Tests

By default, the WebDriver session ends and browser closes after tests finish.

**Recommended ways to keep it open:**

* Use an interactive input prompt after tests (shown above).
* Use a long sleep before `driver.quit()`.
* Run the test script standalone (not via pytest) and add manual pauses.

---

## Example `conftest.py`

```python
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    input("Press Enter to close the browser...")
    driver.quit()
```

---

## Contributing

Feel free to submit issues or pull requests if you find bugs or want to improve functionality.

---

## License

This project is open source under the MIT License.

---

If you want me to help generate or update any specific part of the project, just ask!
