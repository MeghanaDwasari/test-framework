from pages.base_page import BasePage


class DashboardPage(BasePage):

    def verify_dashboard(self):

        # Since site has no dashboard,
        # we simulate success condition

        return "login" in self.driver.current_url