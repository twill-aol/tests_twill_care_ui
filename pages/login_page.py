from .base_page import BasePage
from .locators import LoginPageLocators
from .uri import URI


class LoginPageLocators(BasePage):
    def should_be_elements_on_main_page(self):
        pass
        # self.is_elements_present(
        #     (
        #         MainPageLocators.ARTICLES_LINK,
        #         MainPageLocators.EXPERTS_LINK,
        #         MainPageLocators.LOGIN_LINK,
        #         MainPageLocators.SIGNUP_LINK,
        #     )
        # )

    def go_to_links_on_main_page(self):
        pass
        # self.go_to_links(
        #     {
        #         MainPageLocators.ARTICLES_LINK: URI['articles'],
        #         MainPageLocators.EXPERTS_LINK: URI['experts'],
        #         MainPageLocators.LOGIN_LINK: URI['login'],
        #         MainPageLocators.SIGNUP_LINK: URI['signup'],
        #     }
        # )
