from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait_title, assert_element


def test_check_monitors(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=20_27&product_id=41")
    wait_title("iMac", browser)
    assert_element("[id='button-cart']", browser)
    assert_element("[class='rating']", browser)
    assert_element("[id='input-quantity']", browser)
    assert_element("[id='cart-total']", browser)
    assert_element("[class='navbar-header']", browser)
    WebDriverWait(browser, 2).until(EC.text_to_be_present_in_element((By.ID, "content"), "Related Products"))
    WebDriverWait(browser, 2).until(EC.text_to_be_present_in_element((By.ID, "logo"), "Your Store"))
