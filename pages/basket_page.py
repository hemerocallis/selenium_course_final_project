from .base_page import BasePage
from .locators import BasketPageLocators
from .string_resources import BasketPageStringResources

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_label()
        self.should_be_basket_breadcrumb()

    def should_be_basket_url(self):
        basket_url_substring = "basket"
        basket_url = self.browser.current_url
        assert basket_url_substring in basket_url,\
         f"Incorrect basket URL: '{basket_url_substring}' is not a substring of '{basket_url}'"

    def should_be_basket_label(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_LABEL),\
        "Basket label is not presented"

    def should_be_basket_breadcrumb(self):
        basket_breadcrumb = self.browser.find_element(*BasketPageLocators.BASKET_BREADCRUMB)
        basket_breadcrumb_text = basket_breadcrumb.text
        expected_breadcrumb = BasketPageStringResources.BASKET_BREADCRUMB_TEXT_EN

        assert self.is_element_present(*BasketPageLocators.BASKET_BREADCRUMB),\
        "Basket breadcrumb is not presented"

        assert basket_breadcrumb_text == expected_breadcrumb,\
        f"Basket breadcrumb is incorrect. Expected: '{expected_breadcrumb}', actual: '{basket_breadcrumb_text}"

    # check: there is no product in the basket
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_SECTION),\
        "At least one basket item is present, but should not"

    # check: there is text about empty basket
    def should_be_empty_basket_text(self):
        empty_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        empty_basket_text = empty_basket.text
        expected_basket_text = BasketPageStringResources.EMPTY_BASKET_TEXT_EN

        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT),\
        "Empty basket text is not presented"

        assert empty_basket_text == expected_basket_text,\
        f"Epmty basket has incorrect text. Expected: '{expected_basket_text}', actual: '{empty_basket_text}'"
