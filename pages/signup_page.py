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

    def back_button_missing_during_open_signup_page_by_direct_link(self):
        assert self.is_not_element_present(SignupPageLocators.BACK_BUTTON), \
            'Back button is present on signup page'

    def back_button_presents_during_open_signup_page_by_go_from_main_page(self):
        self.click_active_element(MainPageLocators.LOGIN_LINK, URI['login'])
        assert self.is_element_present(SignupPageLocators.BACK_BUTTON), \
            'Back button is missing on signup page'
