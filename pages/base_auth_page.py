from .base_page import BasePage
from .locators import BaseAuthPageLocators


class BaseAuthPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*BaseAuthPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_flag = "login"
        login_url = self.browser.current_url
        assert login_flag in login_url, f"{login_flag} is not in URL: {login_url}"

    def should_be_register_form(self):
        assert self.is_element_present(*BaseAuthPageLocators.REGISTER_FORM), "Register form is not presented"
