import pytest

from book_store.pages.main_page import MainPage
from book_store.constants.text_elements import empty_basket_text


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_29?promo=midsummer"
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_login_link()


@pytest.mark.parametrize("language", [*empty_basket_text.keys()])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}"
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_basket_via_cite_header_button()
    page.check_basket_is_empty()
    page.check_empty_basket_text(empty_basket_text[language])
