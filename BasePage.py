from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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


def present_element(selector, text_element, driver, timeout=2):
    try:
        WebDriverWait(driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, selector), text_element))
    except TimeoutException:
        raise AssertionError("Отсутствует элемент: {} с текстом {}".format(selector, text_element))
