from .main_page import MainPage
from .locators import ProductPageLocators


class ProductPage(MainPage):

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
        add_to_basket_button.click()

    def check_added_to_basket_product_name(self):
        product_name_from_alert = (self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_IN_ALERT)).text
        product_name_from_page = (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE)).text
        assert product_name_from_alert == product_name_from_page, \
            f"Added product name is: {product_name_from_alert}, not expected {product_name_from_page}"

    def check_total_price_in_basket(self):
        total_basket_price = (self.browser.find_element(*ProductPageLocators.PRODUCTS_IN_BASKET_PRICE)).text
        product_price_from_page = (self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE)).text
        assert total_basket_price == product_price_from_page, \
            f"Actual basket price is: {total_basket_price}, not expected {product_price_from_page}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_success_message_disappeared(self):
        assert self.is_element_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
