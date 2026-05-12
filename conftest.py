import pytest
from _pytest.fixtures import SubRequest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def driver(request: SubRequest):
    if request.config.getoption('--browser') == 'FF':
        driver = webdriver.Firefox()
    elif request.config.getoption('--browser') == 'chrome':
        driver = webdriver.Chrome()
    yield driver
    driver.quit()
