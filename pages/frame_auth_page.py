import pytest
from .base_page import BasePage
from .locators import BaseAuthPageLocators
from .uri import URI
from pages.data import DATA
from pages.messages import MESSAGES


class FrameAuthPage(BasePage):
    def should_be_elements_on_frame_auth_page(self):
        self.is_elements_present(
            (
                BaseAuthPageLocators.LOGO_LINK,
                BaseAuthPageLocators.TOP_NAV,
                BaseAuthPageLocators.SEARCH_BUTTON,
                BaseAuthPageLocators.SAVED_POSTS_BUTTON,
                BaseAuthPageLocators.NOTIFICATIONS_BUTTON,
                # BaseAuthPageLocators.USER_MENU_LINK,
                BaseAuthPageLocators.CREATE_POST_BUTTON,
                # BaseAuthPageLocators.FEED_BUTTON,
                # BaseAuthPageLocators.EXPLORE_BUTTON,
                # BaseAuthPageLocators.TOOLS_BUTTON,
                # BaseAuthPageLocators.MORE_BUTTON,
                BaseAuthPageLocators.FACEBOOK_LINK,
                BaseAuthPageLocators.INSTAGRAM_LINK,
                # BaseAuthPageLocators.ADDITIONAL_INFO_LINK,
            )
        )

    def active_elements_on_frame_auth_page(self):
        self.click_active_elements(
            {
                BaseAuthPageLocators.LOGO_LINK: URI['feed-communities'],
                BaseAuthPageLocators.TOP_NAV: URI['feed-communities'],
                BaseAuthPageLocators.SEARCH_BUTTON: URI['search'],
                BaseAuthPageLocators.SAVED_POSTS_BUTTON: URI['feed-saved'],
                BaseAuthPageLocators.NOTIFICATIONS_BUTTON: URI['notifications'],
                # BaseAuthPageLocators.USER_MENU_LINK: None,
                BaseAuthPageLocators.CREATE_POST_BUTTON: URI['create-post'],
                # BaseAuthPageLocators.FEED_BUTTON: URI['feed-communities'],
                # BaseAuthPageLocators.EXPLORE_BUTTON: URI['articles'],
                # BaseAuthPageLocators.TOOLS_BUTTON: URI['tools'],
                # BaseAuthPageLocators.MORE_BUTTON: None,
                BaseAuthPageLocators.FACEBOOK_LINK: 'facebook',
                BaseAuthPageLocators.INSTAGRAM_LINK: 'instagram',
                # BaseAuthPageLocators.ADDITIONAL_INFO_LINK: URI['disclaimer'],
            }
        )

    def asd(self):
        assert True

    def elements_on_frame_auth_page(self):
        self.login(url = URI['login'])
        print('► 1')
        self.should_be_elements_on_frame_auth_page()
        print('► 2')
        self.asd()
        # self.active_elements_on_frame_auth_page()
        print('► 3')
