from BasePage import assert_element, wait_title, present_element


def test_check_monitors(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=20_27&product_id=41")
    wait_title("iMac", browser)
    assert_element("[id='button-cart']", browser)
    assert_element("[class='rating']", browser)
    assert_element("[id='input-quantity']", browser)
    assert_element("[id='cart-total']", browser)
    assert_element("[class='navbar-header']", browser)
    present_element("#content", "Related Products", browser)
    present_element("#logo", "Your Store", browser)
