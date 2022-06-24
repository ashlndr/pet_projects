from .pages.login_page import LoginPage


def test_should_be_login_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open_page()
    page.should_be_login_forms()


def test_should_be_registration_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open_page()
    page.should_be_registration_forms()


def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open_page()
    page.should_be_login_url()
