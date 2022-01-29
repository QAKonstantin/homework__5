from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait_title, assert_element


def test_check_laptops(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=18")
    wait_title("Laptops & Notebooks", browser)
    assert_element("[class='input-group-addon']", browser)
    assert_element("[class='fa fa-th']", browser)
    assert_element("[class='img-responsive']", browser)
    assert_element("[class='breadcrumb']", browser)
    WebDriverWait(browser, 2).until(EC.text_to_be_present_in_element((By.ID, "content"), "Refine Search"))
    WebDriverWait(browser, 2).until(EC.text_to_be_present_in_element((By.ID, "logo"), "Your Store"))
