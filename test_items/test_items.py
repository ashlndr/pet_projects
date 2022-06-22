from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button_displayed(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    basket_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit'].btn-add-to-basket")
    assert basket_button.is_displayed(), "Basket button must be displayed"
