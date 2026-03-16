from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:

    def __init__(self, driver, timeout=10):

        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )