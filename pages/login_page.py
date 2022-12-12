from .base_page import BasePage
from .locators import LoginPageLocators
from .uri import URI


class LoginPage(BasePage):
    def should_be_elements_on_login_page(self):
        self.is_elements_present(
            (
                LoginPageLocators.LOGIN_FORM,
                LoginPageLocators.EMAIL_FIELD,
                LoginPageLocators.PASSWORD_FIELD,
                LoginPageLocators.SIGN_IN_BUTTON,
                LoginPageLocators.SIGN_IN_FACEBOOK_BUTTON,
                LoginPageLocators.SIGN_IN_APPLE_BUTTON,
                LoginPageLocators.FORGOT_PASSWORD_LINK,
                LoginPageLocators.BACK_BUTTON,
            )
        )

    def active_elements_on_login_page(self):
        self.go_to_active_elements(
            {
                LoginPageLocators.SIGN_IN_BUTTON: URI['login'],
                LoginPageLocators.SIGN_IN_FACEBOOK_BUTTON: 'facebook',
                LoginPageLocators.SIGN_IN_APPLE_BUTTON: 'apple',
                LoginPageLocators.FORGOT_PASSWORD_LINK: URI['forgot_password'],
            }
        )

    def wrong_data_to_login(self):
        self.go_to_active_element(LoginPageLocators.SIGN_IN_BUTTON, URI['login'])
        error_message = self.return_element_text(LoginPageLocators.ERROR_MESSAGE)
        except_error_message = 'The email and password you entered did not \
            match our records. Please try again or click "Forgot Password?"'
        assert error_message == except_error_message, \
            f'Excpected error message does not match: \nerror_message:[{error_message}] \
            \nexcept_error_message[{except_error_message}]'

    def back_button_missing_during_open_login_page_by_direct_link(self):
        self.is_element_present(LoginPageLocators.BACK_BUTTON)

    def login_user(self):
        # api_register
        pass

# LOGIN_FORM
# EMAIL_FIELD
# PASSWORD_FIELD
# SIGN_IN_BUTTON
# SIGN_IN_FACEBOOK_BUT
# SIGN_IN_APPLE_BUTTON
# FORGOT_PASSWORD_LINK
# BACK_BUTTON