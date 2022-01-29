from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait_title, assert_element


def test_check_phones(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=24")
    wait_title("Phones & PDAs", browser)
    assert_element("[class='list-group-item active']", browser)
    assert_element("[id='column-left']", browser)
    assert_element("[id='search']", browser)
    assert_element("[id='content']", browser)
    assert_element("[id='cart-total']", browser)
    WebDriverWait(browser, 3).until(
        EC.text_to_be_present_in_element((By.ID, "logo"), "Your Store"))
    WebDriverWait(browser, 3).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "breadcrumb"), "Phones & PDAs"))
