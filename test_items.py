import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)

    time.sleep(3)
    try:
        browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        button_exist = True
    except Exception:
        button_exist = False

    assert button_exist is True, "Element doesn't exist on page!"
