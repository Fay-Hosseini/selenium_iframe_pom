from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IframePage(BasePage):
    URL = "https://practice.expandtesting.com/iframe"

    INTERNAL_IFRAME = (By.ID, "email-subscribe")
    EXTERNAL_IFRAME = (By.ID, 'mce_0_ifr')
    VIDEO_IFRAME = (By.ID, 'iframe-youtube')

    SUBSCRIBE_EMAIL_INPUT = (By.ID, "email")
    SUBSCRIBE_BUTTON = (By.ID, "btn-subscribe")

    def load(self):
        self.goto(self.URL)

    def subscribe_inner_iframe(self, email):

        #  # Print all iframes on the current page (top-level)
        # iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        # print(f"Number of iframes on page: {len(iframes)}")
        # for i, iframe in enumerate(iframes):
        #     print(f"Iframe {i}: id={iframe.get_attribute('id')}, name={iframe.get_attribute('name')}")
        wait = WebDriverWait(self.driver, 10)

        # Switch to the iframe first
        wait.until(EC.frame_to_be_available_and_switch_to_it(self.INTERNAL_IFRAME))

        # # Debug print the HTML inside the iframe context
        # print(self.driver.page_source)

        # Wait for email input to be visible, then send keys
        email_input = wait.until(EC.visibility_of_element_located(self.SUBSCRIBE_EMAIL_INPUT))
        email_input.send_keys(email)

        # Optionally switch back to main content after interaction
        #self.driver.switch_to.default_content()

    def check_youtube_iframe_presence(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located(self.VIDEO_IFRAME))
            return True
        except TimeoutException:
            return False


