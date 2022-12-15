from .base_page import BasePage
from .locators import MainPageLocators
from .uri import URI


class MainPage(BasePage):
    def should_be_elements_on_main_page(self):
        self.is_elements_present(
            (
                MainPageLocators.ARTICLES_LINK,
                MainPageLocators.EXPERTS_LINK,
                MainPageLocators.LOGIN_LINK,
                MainPageLocators.SIGNUP_LINK,
            )
        )

    def active_elements_on_main_page(self):
        self.click_active_elements(
            {
                MainPageLocators.ARTICLES_LINK: URI['articles'],
                MainPageLocators.EXPERTS_LINK: URI['experts'],
                MainPageLocators.LOGIN_LINK: URI['login'],
                MainPageLocators.SIGNUP_LINK: URI['signup'],
            }
        )
