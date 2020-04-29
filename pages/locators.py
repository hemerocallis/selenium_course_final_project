from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_LABEL = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_IN_BASKET_ALERT = (By.CSS_SELECTOR, "div.alert-success div.alertinner strong")
    PRODUCT_PRICE_LABEL = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE_ALERT = (By.CSS_SELECTOR, "div.alert-info div.alertinner p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group")

class BasketPageLocators():
    BASKET_LABEL = (By.CSS_SELECTOR, "div.page-header h1")
    EMPTY_BASKET_TEXT = (By.XPATH, "//div[@id='content_inner']/p")
    BASKET_BREADCRUMB = (By.XPATH, "//li[@class='active']")
    BASKET_ITEMS_SECTION = (By.CSS_SELECTOR, "div.basket-items")
