from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_correct_product_name(self):
        alert_success = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT)
        alert_text = alert_success.text
        product_name_label = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LABEL)
        product_name = product_name_label.text

        assert product_name in alert_text, "Incorrect product name"

    def should_be_correct_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_LABEL)
        product_price_text = product_price.text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_ALERT)
        basket_price_text = basket_price.text

        assert product_price_text == basket_price_text, "Incorrect basket price"


