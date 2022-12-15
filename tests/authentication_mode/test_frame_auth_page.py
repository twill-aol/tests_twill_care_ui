from pages.frame_auth_page import FrameAuthPage
from pages.uri import URI
# import allure


def test_elements_on_page_frame(browser, main_url):
    page = FrameAuthPage(browser, main_url + URI['login'])
    page.open()
    page.elements_on_frame_auth_page()
