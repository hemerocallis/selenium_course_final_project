from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()

    product_name = product_page.get_product_name()
    product_page.should_be_correct_product_name(product_name)

    product_price = product_page.get_product_price()
    product_page.should_be_correct_basket_price(product_price)
