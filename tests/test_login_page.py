from pages.main_page import LoginPage
from pages.uri import URI
import allure


def test_elements_on_main_page(browser, main_url):
    page = LoginPage(browser, main_url)
    page.open()
    page.should_be_elements_on_main_page()

def test_go_to_links_on_main_page(browser, main_url):
    page = LoginPage(browser, main_url)
    page.open()
    page.go_to_links_on_main_page()
