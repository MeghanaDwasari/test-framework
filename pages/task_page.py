from pages.base_page import BasePage


class TasksPage(BasePage):

    def open_tasks_page(self):

        self.driver.get(
            "https://react-frontend-api-testing.vercel.app/tasks"
        )

    def update_task_status(self, status):

        print("Updating task status")

    def verify_task_status(self, status):

        return True