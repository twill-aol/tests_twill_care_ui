from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_link(self):
        login_flag = "login"
        login_url = self.browser.current_url
        assert login_flag in login_url, f"{login_flag} is not in URL: {login_url}"

    def should_be_elements_on_main_page(self):
        assert self.is_elements_present(
            (
                MainPageLocators.ARTICLES_LINK,
                MainPageLocators.EXPERTS_LINK,
                MainPageLocators.LOGIN_LINK,
                MainPageLocators.SIGNUP_LINK,
            )
        ), 'Elements not found in Main page'
