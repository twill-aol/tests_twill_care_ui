from pages.main_page import MainPage
from pages.uri import URI
# import allure


def test_elements_on_main_page(browser, main_url):
    page = MainPage(browser, main_url)
    page.open()
    page.should_be_elements_on_main_page()

def test_active_elements_on_main_page(browser, main_url):
    page = MainPage(browser, main_url)
    page.open()
    page.active_elements_on_main_page()
