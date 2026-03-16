from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    ADMIN_BTN = (By.XPATH, "//button[contains(text(),'Admin')]")
    USER_BTN = (By.XPATH, "//button[contains(text(),'User')]")

    def login_as_admin(self):
        self.driver.find_element(*self.ADMIN_BTN).click()

    def login_as_user(self):
        self.driver.find_element(*self.USER_BTN).click()

    def enter_credentials(self, email, password):
        # demo site has no inputs so simulate
        pass

    def click_login(self):
        pass

    def is_login_page(self):
        return "login" in self.driver.current_url