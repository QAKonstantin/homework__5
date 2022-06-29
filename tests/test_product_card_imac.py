from BasePage import assert_element, wait_title, present_element


def test_check_card_imac(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=20_27&product_id=41")
    wait_title("iMac", browser)
    assert_element("[class='product-thumb transition']", browser)
    assert_element("[id='top']", browser)
    assert_element("[id='search']", browser)
    assert_element("[id='input-quantity']", browser)
    assert_element("[class='breadcrumb']", browser)
    present_element("#logo", "Your Store", browser)
    present_element(".active", "Description", browser)
    present_element("#button-cart", "Add to Cart", browser)
