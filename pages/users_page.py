from pages.base_page import BasePage


class UsersPage(BasePage):

    def open_users_page(self):

        self.driver.get(
            "https://react-frontend-api-testing.vercel.app/"
        )

    def verify_users_page(self):

        # demo validation
        return "vercel" in self.driver.current_url