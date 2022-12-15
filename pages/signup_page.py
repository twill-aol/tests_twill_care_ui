from .base_page import BasePage
from .locators import SignupPageLocators, MainPageLocators
from .uri import URI


class SignupPage(BasePage):
    def should_be_elements_on_signup_page(self):
        self.is_elements_present(
            (
                SignupPageLocators.EMAIL_FIELD,
                SignupPageLocators.PRIVACY_CHECK_BUTTON,
                SignupPageLocators.TAC_LINK,
                SignupPageLocators.PP_LINK,
                SignupPageLocators.SIGNUP_BUTTON,
                SignupPageLocators.SIGNUP_FACEBOOK_BUTTON,
                SignupPageLocators.SIGNUP_APPLE_BUTTON,
            )
        )

    def active_elements_on_signup_page(self):
        self.click_active_elements(
            {
                SignupPageLocators.PRIVACY_CHECK_BUTTON: None,
                SignupPageLocators.EMAIL_FIELD: None,
                SignupPageLocators.SIGNUP_BUTTON: URI['signup'],
                SignupPageLocators.TAC_LINK: URI['tac'],
                SignupPageLocators.PP_LINK: URI['privacy_policy'],
                # SignupPageLocators.PRIVACY_CHECK_BUTTON: None,
                # SignupPageLocators.SIGNUP_FACEBOOK_BUTTON: 'facebook',
                # SignupPageLocators.PRIVACY_CHECK_BUTTON: None,
                # SignupPageLocators.SIGNUP_APPLE_BUTTON: 'apple',
            }
        )

    def button_sugnup_apple_on_signup_page(self):
        self.click_active_elements(
            {
                SignupPageLocators.PRIVACY_CHECK_BUTTON: None,
                SignupPageLocators.SIGNUP_APPLE_BUTTON: 'apple',
            }
        )

    def button_sugnup_facebook_on_signup_page(self):
        self.click_active_elements(
            {
                SignupPageLocators.PRIVACY_CHECK_BUTTON: None,
                SignupPageLocators.SIGNUP_FACEBOOK_BUTTON: 'facebook',
            }
        )
