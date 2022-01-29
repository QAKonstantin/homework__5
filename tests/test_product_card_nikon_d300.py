from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait_title, assert_element


def test_check_card_nikon_d300(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=33&product_id=31")
    wait_title("Nikon D300", browser)
    assert_element("[class='cpt_product_description ']", browser)
    assert_element("[id='top']", browser)
    assert_element("[id='search']", browser)
    assert_element("[id='input-quantity']", browser)
    assert_element("[class='breadcrumb']", browser)
    WebDriverWait(browser, 3).until(
        EC.text_to_be_present_in_element((By.ID, "logo"), "Your Store"))
    WebDriverWait(browser, 3).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "active"), "Description"))
    WebDriverWait(browser, 3).until(
        EC.text_to_be_present_in_element((By.ID, "button-cart"), "Add to Cart"))
