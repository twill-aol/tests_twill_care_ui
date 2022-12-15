from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators
from .uri import URI
from pages.messages import MESSAGES


class LoginPage(BasePage):
    def should_be_elements_on_login_page(self):
        self.is_elements_present(
            (
                LoginPageLocators.LOGIN_FORM,
                LoginPageLocators.EMAIL_FIELD,
                LoginPageLocators.PASSWORD_FIELD,
                LoginPageLocators.SIGNIN_BUTTON,
                LoginPageLocators.SIGNIN_FACEBOOK_BUTTON,
                LoginPageLocators.SIGNIN_APPLE_BUTTON,
                LoginPageLocators.FORGOT_PASSWORD_LINK,
            )
        )

    def active_elements_on_login_page(self):
        self.click_active_elements(
            {
                LoginPageLocators.SIGNIN_BUTTON: URI['login'],
                LoginPageLocators.SIGNIN_FACEBOOK_BUTTON: 'facebook',
                LoginPageLocators.SIGNIN_APPLE_BUTTON: 'apple',
                LoginPageLocators.FORGOT_PASSWORD_LINK: URI['forgot_password'],
            }
        )

    def wrong_data_to_login(self):
        # check with empty fields
        self.click_active_element(LoginPageLocators.SIGNIN_BUTTON, URI['login'])
        error_message = self.return_element_text(LoginPageLocators.ERROR_MESSAGE)
        except_error_message = MESSAGES['login_wrong']
        assert self.text_match((except_error_message, error_message))

    def back_button_missing_during_open_login_page_by_direct_link(self):
        assert self.is_not_element_present(LoginPageLocators.BACK_BUTTON), \
            'Back button is present on login page'

    def back_button_presents_during_open_login_page_by_go_from_main_page(self):
        self.click_active_element(MainPageLocators.LOGIN_LINK, URI['login'])
        assert self.is_element_present(LoginPageLocators.BACK_BUTTON), \
            'Back button is missing on login page'

    def login_user(self):
        # email_new_user = api_register
        assert self.login(), 'Login failed'
