from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait_title, assert_element


def test_check_main_page(browser):
    wait_title("Your Store", browser)
    assert_element("[id='slideshow0']", browser)
    assert_element("[id='carousel0']", browser)
    assert_element("[id='search']", browser)
    assert_element("[class='row']", browser)
    assert_element("[class='collapse navbar-collapse navbar-ex1-collapse']", browser)
    WebDriverWait(browser, 3).until(
        EC.text_to_be_present_in_element((By.ID, "logo"), "Your Store"))
    WebDriverWait(browser, 3).until(
        EC.text_to_be_present_in_element((By.ID, "cart-total"), "0 item(s) - $0.00"))
