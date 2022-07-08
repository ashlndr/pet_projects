from book_store.constants.links import login_page_link
from book_store.pages.login_page import LoginPage


def test_should_be_login_forms(browser):
    link = login_page_link
    page = LoginPage(browser, link)
    page.open_page()
    page.should_be_login_forms()


def test_should_be_registration_forms(browser):
    link = login_page_link
    page = LoginPage(browser, link)
    page.open_page()
    page.should_be_registration_forms()


def test_should_be_login_url(browser):
    link = login_page_link
    page = LoginPage(browser, link)
    page.open_page()
    page.should_be_login_url()
