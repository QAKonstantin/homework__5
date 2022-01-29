import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("C:/drivers1"))


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=drivers + "/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=drivers + "/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    else:
        driver = webdriver.Safari()

    driver.maximize_window()
    request.addfinalizer(driver.close)
    driver.get(url)
    driver.url = url
    return driver


def wait_title(title, driver, timeout=2):
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        raise AssertionError("Ожидал title: '{}', но получил такой: '{}'".format(title, driver.title))


def assert_element(selector, driver, timeout=2):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        raise AssertionError("Отсутствует видимость элемента: {}".format(selector))
