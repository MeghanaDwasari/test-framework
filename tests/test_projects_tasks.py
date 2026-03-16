from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.task_page import TasksPage


# TC05 - Project Creation Flow
def test_project_creation_flow(driver):

    login = LoginPage(driver)
    login.login_as_admin()

    projects = ProjectsPage(driver)

    projects.open_projects_page()
    projects.create_project("Automation Project", "Selenium Testing")

    assert projects.verify_project_created("Automation Project")


# TC06 - Task Status Update
def test_task_status_update(driver):

    login = LoginPage(driver)
    login.login_as_admin()

    tasks = TasksPage(driver)

    tasks.open_tasks_page()
    tasks.update_task_status("In Progress")

    assert tasks.verify_task_status("In Progress")