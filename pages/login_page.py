from .base_page import BasePage
from .locators import LoginPageLocators
from .uri import URI


class MainPage(BasePage):
    def should_be_elements_on_main_page(self):
        pass
        # self.is_elements_present(
        #     (
        #         LoginPageLocators.ARTICLES_LINK,
        #     )
        # )

    def go_to_links_on_main_page(self):
        pass
        # self.go_to_links(
        #     {
        #         LoginPageLocators.ARTICLES_LINK: URI['articles'],
        #     }
        # )
