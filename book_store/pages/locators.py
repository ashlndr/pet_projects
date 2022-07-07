from selenium.webdriver.common.by import By


class BasePageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:

    FORM_USERNAME = (By.ID, "id_login-username")
    FORM_PASSWORD = (By.ID, "id_login-password")
    REGISTER_FORM_EMAIL = (By.ID, "id_registration-email")
    REGISTER_FORM_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_FORM_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")


class ProductPageLocators:

    PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDED_PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCTS_IN_BASKET_PRICE = (By.CSS_SELECTOR, "div.alert.alert-info > div > p:nth-child(1) > strong")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, "div.product_main h1:nth-child(n)")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div:nth-child(1)")
