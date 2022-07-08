from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_forms()
        self.should_be_registration_forms()

    def should_be_login_url(self):
        expected_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        actual_url = self.browser.current_url
        assert actual_url == expected_url, "Actual url is not expected one"

    def should_be_login_forms(self):
        assert self.is_element_present(*LoginPageLocators.FORM_USERNAME), "Login username form is not presented"
        assert self.is_element_present(*LoginPageLocators.FORM_PASSWORD), "Login password form is not presented"

    def should_be_registration_forms(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL), \
            "Login registration email form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD), \
            "Login registration password form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD), \
            "Login registration confirm password form is not presented"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password_confirm_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        email_form.send_keys(email)
        password_form.send_keys(password)
        password_confirm_form.send_keys(password)
        submit_button.click()
        self.is_not_element_present(*LoginPageLocators.SUCCESSFUL_REGISTRATION, timeout=20)
