import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize("offer_type", ["offer0", "offer1", "offer2", "offer3", "offer4",
                                        "offer5", "offer6", "offer7", "offer8", "offer9",
                                        pytest.param("offer7", marks=pytest.mark.xfail),
                                        ])
def test_add_product_to_basket(browser, offer_type):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer_type}"
    page = ProductPage(browser, link)
    page.open_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_to_basket_product_name()
    page.check_total_price_in_basket()
