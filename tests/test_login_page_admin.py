from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait_title, assert_element


def test_check_page_admin(browser):
    browser.get("https://demo.opencart.com/admin")
    wait_title("Administration", browser)
    assert_element("[class='fa fa-user']", browser)
    assert_element("[class='input-group']", browser)
    assert_element("[class='btn btn-primary']", browser)
    assert_element("[href='https://demo.opencart.com/admin/index.php?route=common/forgotten']", browser)
    assert_element("[class='panel-body']", browser)
    WebDriverWait(browser, 2).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "panel-heading"), "Please enter your login details."))
    WebDriverWait(browser, 2).until(
        EC.text_to_be_present_in_element((By.ID, "footer"), " © 2009-2022 All Rights Reserved."))
