import math

from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_via_cite_header_button(self):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_button.click()

    def check_empty_basket_text(self, language_text):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_IS_EMPTY_ELEMENT)
        assert language_text in basket_button.text, f"Actual basket text is: {basket_button.text}."

    def check_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY_ELEMENT), "Basket is not empty!"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def wait_for_element(self, how, what):
        try:
            element = WebDriverWait(self.browser, timeout=10, poll_frequency=1).until(
                EC.presence_of_element_located(
                    (how, what))
            )
        except NoSuchElementException as ex:
            raise ex
        return element

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
