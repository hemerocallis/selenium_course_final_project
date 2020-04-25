BASE_URL = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

# pytest -v --tb=line --language=en test_main_page.py
def test_guest_can_go_to_login_page(browser):
    browser.get(BASE_URL)
    go_to_login_page(browser)
