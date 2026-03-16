from selenium.webdriver.common.by import By


class LoginLocators:

    ADMIN_BTN = (By.XPATH, "//button[contains(.,'Admin')]")
    USER_BTN = (By.XPATH, "//button[contains(.,'User')]")

class DashboardLocators:

    TITLE = (By.XPATH, "//h1")

class ProjectLocators:

    CREATE_BTN = (By.ID, "create-project")

class TaskLocators:

    STATUS = (By.CLASS_NAME, "task-status")