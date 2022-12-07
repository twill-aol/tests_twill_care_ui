import math
from .locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException, TimeoutException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def _is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True

    def is_elements_present(self, elements):
        not_found_elements = []
        for element in elements:
            how, what = element
            if not self.is_element_present(how, what):
                not_found_elements.append(what)
        if len(not_found_elements):
            try:
                assert False, f'Elements not found: {not_found_elements}'
            finally:
                return False

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_not_elements_present(self, elements, timeout=4):
        found_elements = []
        for element in elements:
            how, what = element
            if not self.is_not_element_present(how, what):
                found_elements.append(what)
        if len(found_elements):
            try:
                assert False, f'Elements not found: {found_elements}'
            finally:
                return False

    def open(self):
        self.browser.get(self.url)

    def return_element_text(self, how, what):
        try:
            data = self.browser.find_element(how, what).text
        except:
            return False
        return data

    def finder_text(self, content, flag, board):
        find_id_position = content.find(flag) + len(flag)
        text = ""
        for symbol in content[find_id_position:]:
            if symbol != board:
                text += symbol
            else:
                break
        return text
