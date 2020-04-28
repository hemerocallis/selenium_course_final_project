from .pages.product_page import ProductPage
import pytest
import time

# @pytest.mark.xfail(reason="fixing is planned in sprint 'Never'")
@pytest.mark.skip(reason="\nblocked test")
@pytest.mark.parametrize('link_item', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, link_item):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_item}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_seccess_message()
    product_page.add_product_to_basket()

    product_name = product_page.get_product_name()
    product_page.should_be_correct_product_name(product_name)

    product_price = product_page.get_product_price()
    product_page.should_be_correct_basket_price(product_price)

@pytest.mark.skip(reason="\nblocked test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_seccess_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_seccess_message()

@pytest.mark.xfail(reason="bug fixing is in progress")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_disappeared_success_message()
