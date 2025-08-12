import tempfile
import time

import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    # e.g., options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # no user-data-dir here
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()      # Maximize here
    driver.implicitly_wait(5)
    yield driver
    # Comment out driver.quit() to keep the browser open after tests finish
    time.sleep(5)  # keeps the browser open for 10 minutes
    # driver.quit()

