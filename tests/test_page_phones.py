from BasePage import assert_element, wait_title, present_element


def test_check_phones(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=24")
    wait_title("Phones & PDAs", browser)
    assert_element("[class='list-group-item active']", browser)
    assert_element("[id='column-left']", browser)
    assert_element("[id='search']", browser)
    assert_element("[id='content']", browser)
    assert_element("[id='cart-total']", browser)
    present_element("#logo", "Your Store", browser)
    present_element(".breadcrumb", "Phones & PDAs", browser)
