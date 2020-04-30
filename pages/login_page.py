from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url_substring = "login"
        login_url = self.browser.current_url
        assert login_url_substring in login_url, f"Incorrect login URL: '{login_url_substring}' is not a substring of '{login_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not found"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

        confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
