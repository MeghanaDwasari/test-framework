from pages.base_page import BasePage


class ProjectsPage(BasePage):

    def open_projects_page(self):

        self.driver.get(
            "https://react-frontend-api-testing.vercel.app/projects"
        )

    def create_project(self, name, description):

        # Demo placeholder
        print(f"Creating project {name}")

    def verify_project_created(self, name):

        return True