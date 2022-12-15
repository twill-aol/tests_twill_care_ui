from pages.signup_page import SignupPage
from pages.uri import URI
# import allure


def test_elements_on_signup_page(browser, main_url):
    page = SignupPage(browser, main_url + URI['signup'])
    page.open()
    page.should_be_elements_on_signup_page()

def test_active_elements_on_signup_page(browser, main_url):
    page = SignupPage(browser, main_url + URI['signup'])
    page.open()
    page.active_elements_on_signup_page()

def test_button_sugnup_apple_on_signup_page(browser, main_url):
    page = SignupPage(browser, main_url + URI['signup'])
    page.open()
    page.button_sugnup_apple_on_signup_page()

def test_button_sugnup_facebook_signup_page(browser, main_url):
    page = SignupPage(browser, main_url + URI['signup'])
    page.open()
    page.button_sugnup_facebook_on_signup_page()

def test_back_button_missing_during_open_signup_page_by_direct_link(browser, main_url):
    page = SignupPage(browser, main_url + URI['signup'])
    page.open()
    page.back_button_missing_during_open_signup_page_by_direct_link()

def test_back_button_presents_during_open_signup_page_by_go_from_main_page(browser, main_url):
    page = SignupPage(browser, main_url)
    page.open()
    page.back_button_presents_during_open_signup_page_by_go_from_main_page()
