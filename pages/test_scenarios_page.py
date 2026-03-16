from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ScenariosPage(BasePage):

    def open_scenarios_page(self):

        self.driver.get(
            "https://the-internet.herokuapp.com/javascript_alerts"
        )

    def handle_alert(self):

        self.driver.find_element(
            By.XPATH,
            "//button[text()='Click for JS Alert']"
        ).click()

        alert = self.driver.switch_to.alert
        alert.accept()

    def handle_confirm(self):

        self.driver.find_element(
            By.XPATH,
            "//button[text()='Click for JS Confirm']"
        ).click()

        alert = self.driver.switch_to.alert
        alert.accept()

    def handle_prompt(self, text):

        self.driver.find_element(
            By.XPATH,
            "//button[text()='Click for JS Prompt']"
        ).click()

        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def verify_alert_result(self):

        return "successfully" in self.driver.page_source