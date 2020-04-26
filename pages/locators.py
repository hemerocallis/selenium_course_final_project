from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_LABEL = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_IN_BASKET_ALERT = (By.CSS_SELECTOR, "div.alert-success div.alertinner")
    PRODUCT_PRICE_LABEL = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE_ALERT = (By.CSS_SELECTOR, "div.alert-info div.alertinner p strong")

