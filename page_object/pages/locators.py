from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM_USERNAME = (By.ID, "id_login-username")
    LOGIN_FORM_PASSWORD = (By.ID, "id_login-password")
    LOGIN_REGISTER_FORM_EMAIL = (By.ID, "id_registration-email")
    LOGIN_REGISTER_FORM_PASSWORD = (By.ID, "id_registration-password1")
    LOGIN_REGISTER_FORM_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")


class ProductPageLocators:
    PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADDED_SUCCESS_ALERT_TITLE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCTS_IN_BASKET_PRICE = (By.CSS_SELECTOR, "div.alert.alert-info > div > p:nth-child(1) > strong")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, "div.product_main h1:nth-child(n)")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, "p.price_color")
