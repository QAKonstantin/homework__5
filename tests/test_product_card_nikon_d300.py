from BasePage import assert_element, wait_title, present_element


def test_check_card_nikon_d300(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=33&product_id=31")
    wait_title("Nikon D300", browser)
    assert_element("[class='cpt_product_description ']", browser)
    assert_element("[id='top']", browser)
    assert_element("[id='search']", browser)
    assert_element("[id='input-quantity']", browser)
    assert_element("[class='breadcrumb']", browser)
    present_element("#logo", "Your Store", browser)
    present_element(".active", "Description", browser)
    present_element("#button-cart", "Add to Cart", browser)
