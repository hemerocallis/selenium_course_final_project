from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_name(self):
        product_name_label = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LABEL)
        product_name = product_name_label.text
        return product_name

    def get_product_price(self):
        product_price_label = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_LABEL)
        product_price = product_price_label.text
        return product_price

    def should_be_correct_product_name(self, product_name):
        alert_success = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT)
        alert_text = alert_success.text
        assert product_name == alert_text,\
        f"Incorrect product name. Expected: {product_name}, actual: {alert_text}"

    def should_be_success_alert(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT),\
        "Success message is not presented, but should"

    def should_be_correct_basket_price(self, product_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_ALERT)
        basket_price_text = basket_price.text
        assert product_price == basket_price_text, "Incorrect basket price"

    def should_not_be_seccess_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT), \
        "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT), \
        "Success message is not disappeared, but should"
