import pytest
from utils.driver_factory import create_driver
from config.settings import BASE_URL


@pytest.fixture
def driver():

    driver = create_driver()

    driver.get(BASE_URL)

    yield driver

    driver.quit()