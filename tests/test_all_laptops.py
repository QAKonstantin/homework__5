from BasePage import assert_element, wait_title, present_element


def test_check_laptops(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=18")
    wait_title("Laptops & Notebooks", browser)
    assert_element("[class='input-group-addon']", browser)
    assert_element("[class='fa fa-th']", browser)
    assert_element("[class='img-responsive']", browser)
    assert_element("[class='breadcrumb']", browser)
    present_element("#content", "Refine Search", browser)
    present_element("#logo1", "Your Store", browser)
