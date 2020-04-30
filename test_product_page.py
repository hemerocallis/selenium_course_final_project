from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# pytest -v --tb=line -m login_guest --language=en test_product_page.py
@pytest.mark.login_guest
class TestLoginFromProductPage():
    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self):
    #     self.product = ProductFactory(title = "Best book")
    #     # create a new product via API
    #     self.link = self.product.link
    #     yield
    #     # teardown steps
    #     self.product.delete()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.add_to_basket_by_user
class TestUserAddToBasketFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, self.login_link)
        login_page.open()
        self.email = str(time.time()) + "@fakemail.info"
        self.password = "Qwerrrty1!"
        login_page.register_new_user(self.email, self.password)
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_seccess_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_seccess_message()
        product_page.add_product_to_basket()

        product_name = product_page.get_product_name()
        product_page.should_be_correct_product_name(product_name)

        product_price = product_page.get_product_price()
        product_page.should_be_correct_basket_price(product_price)


@pytest.mark.skip(reason="\nblocked test")
@pytest.mark.parametrize('link_item', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, link_item):
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

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()

    basket_page.should_not_be_basket_items()
    basket_page.should_be_empty_basket_text()
