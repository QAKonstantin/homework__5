from BasePage import assert_element, wait_title, present_element


def test_check_main_page(browser):
    wait_title("Your Store", browser)
    assert_element("[id='slideshow0']", browser)
    assert_element("[id='carousel0']", browser)
    assert_element("[id='search']", browser)
    assert_element("[class='row']", browser)
    assert_element("[class='collapse navbar-collapse navbar-ex1-collapse']", browser)
    present_element("#logo", "Your Store", browser)
    present_element("#cart-total", "0 item(s) - $0.00", browser)
