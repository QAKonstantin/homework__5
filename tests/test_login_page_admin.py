from BasePage import assert_element, wait_title, present_element


def test_check_page_admin(browser):
    browser.get("https://demo.opencart.com/admin")
    wait_title("Administration", browser)
    assert_element("[class='fa fa-user']", browser)
    assert_element("[class='input-group']", browser)
    assert_element("[class='btn btn-primary']", browser)
    assert_element("[href='https://demo.opencart.com/admin/index.php?route=common/forgotten']", browser)
    assert_element("[class='panel-body']", browser)
    present_element(".panel-heading", "Please enter your login details.", browser)
    present_element("#footer", " © 2009-2022 All Rights Reserved.", browser)
