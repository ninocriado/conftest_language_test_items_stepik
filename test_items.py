from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_basket_visible(browser):
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))
    print(button)
    assert button > 0, "button add to basket not found"

