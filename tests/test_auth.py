import pytest
from pages.login_page import LoginPage


def test_valid_admin_login(driver):

    login = LoginPage(driver)

    login.login_as_admin()

    assert login.is_login_page()


@pytest.mark.parametrize(
    "email,password",
    [
        ("wrong@gmail.com", "wrongpass"),
        ("invalidemail", "password"),
        ("", "")
    ]
)
def test_invalid_login_matrix(driver, email, password):

    login = LoginPage(driver)

    login.enter_credentials(email, password)

    login.click_login()

    assert login.is_login_page()