from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_dashboard_visible(driver):

    login = LoginPage(driver)

    login.login_as_admin()

    dashboard = DashboardPage(driver)

    assert dashboard.verify_dashboard()