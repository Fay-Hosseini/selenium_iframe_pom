class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def goto(self,URL):
        self.driver.get(URL)

    def switch_to_iframe(self,by_locator):
        iframe = self.driver.find_element(*by_locator)
        self.driver.switch_to.frame(iframe)

    def back_to_default(self):
        self.driver.switch_to.default_content()