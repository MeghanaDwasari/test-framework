from pages.login_page import LoginPage
from pages.users_page import UsersPage


# TC03 - Admin Users Page Access
def test_admin_users_page_access(driver):

    login = LoginPage(driver)
    login.login_as_admin()

    users = UsersPage(driver)
    users.open_users_page()

    assert users.verify_users_page()


# TC04 - Non-Admin Access Restriction
def test_non_admin_access_restriction(driver):

    login = LoginPage(driver)
    login.login_as_user()

    users = UsersPage(driver)
    users.open_users_page()

    assert "access" in driver.page_source.lower() or "denied" in driver.page_source.lower() 