from .pages.main_page import MainPage
from .pages.login_page import LoginPage

# pytest -v --tb=line --language=en test_main_page.py
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link) # Page Object initialization
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()
