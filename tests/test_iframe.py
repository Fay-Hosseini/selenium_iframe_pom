import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.iframe_page import IframePage

@pytest.fixture
def driver():
    options = Options()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_internal_button_click(driver):     #receives a Selenium driver fixture (usually from conftest.py)
    page = IframePage(driver)               #creates an IframePage object, passing the driver so the page object can control the browser
    page.load()
    page.subscribe_inner_iframe("test@example.com")

def test_youtube_iframe_presence(driver):
    page = IframePage(driver)               #creates an IframePage object, passing the driver so the page object can control the browser
    page.load()
    assert page.check_youtube_iframe_presence(), "YouTube iframe should be present"