from pages.login_page import LoginPage
from pages.uri import URI
# import allure


def test_elements_on_login_page(browser, main_url):
    page = LoginPage(browser, main_url + URI['login'])
    page.open()
    page.should_be_elements_on_login_page()

def test_active_elements_on_login_page(browser, main_url):
    page = LoginPage(browser, main_url + URI['login'])
    page.open()
    page.active_elements_on_login_page()

def test_wrong_data_to_login(browser, main_url):
    page = LoginPage(browser, main_url + URI['login'])
    page.open()
    page.wrong_data_to_login()

def test_back_button_missing_during_open_login_page_by_direct_link(browser, main_url):
    page = LoginPage(browser, main_url + URI['login'])
    page.open()
    page.back_button_missing_during_open_login_page_by_direct_link()

def test_login(browser, main_url):
    page = LoginPage(browser, main_url + URI['login'])
    page.login_user()
