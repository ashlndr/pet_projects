import pytest

from book_store.constants.links import product_page_link, login_page_link
from book_store.constants.text_elements import empty_basket_text
from book_store.pages.product_page import ProductPage
from book_store.pages.login_page import LoginPage
from book_store.utils.string_generator import generated_email, generated_password


@pytest.mark.authorized_users
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_link = login_page_link
        page = LoginPage(browser, login_link)
        page.open_page()
        page.register_new_user(generated_email(), generated_password())
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = product_page_link
        page = ProductPage(browser, link)
        page.open_page()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = product_page_link
        page = ProductPage(browser, link)
        page.open_page()
        page.add_product_to_basket()
        page.check_added_to_basket_product_name()
        page.check_total_price_in_basket()


def test_guest_cant_see_success_message(browser):
    link = product_page_link
    page = ProductPage(browser, link)
    page.open_page()
    page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize("offer_type", ["offer0", "offer1", "offer2", "offer3", "offer4",
                                        "offer5", "offer6", "offer7", "offer8", "offer9",
                                        pytest.param("offer7", marks=pytest.mark.xfail),
                                        ])
def test_guest_can_add_product_to_basket(browser, offer_type):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer_type}"
    page = ProductPage(browser, link)
    page.open_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_to_basket_product_name()
    page.check_total_price_in_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = product_page_link
    page = ProductPage(browser, link)
    page.open_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = product_page_link
    page = ProductPage(browser, link)
    page.open_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.is_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = product_page_link
    page = ProductPage(browser, link)
    page.open_page()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = product_page_link
    page = ProductPage(browser, link)
    page.open_page()
    page.go_to_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize("language", [*empty_basket_text.keys()])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}"
    page = ProductPage(browser, link)
    page.open_page()
    page.go_to_basket_via_cite_header_button()
    page.check_basket_is_empty()
    page.check_empty_basket_text(empty_basket_text[language])
