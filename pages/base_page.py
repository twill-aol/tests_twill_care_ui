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

    def finder_text(self, content, flag, board):
        find_id_position = content.find(flag) + len(flag)
        text = ""
        for symbol in content[find_id_position:]:
            if symbol != board:
                text += symbol
            else:
                break
        return text

    def go_to_link(self, element, flag=None):
        try:
            link = self.browser.find_element(*element)
            link.click()
            if flag is not None:
                current_url = self.browser.current_url
                assert flag in current_url, f"{flag} is not in URL: {current_url}"
        except:
            return False
        return True

    def go_to_links(self, elements: dict):
        problem_elements = []
        for element in elements:
            flag = elements[element]
            if not self.go_to_link(element, flag):
                problem_elements.append(flag)
            self.browser.back()
        if problem_elements:
            assert False, f'Check links does not have parts: {problem_elements}'

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True

    def is_elements_present(self, elements: tuple):
        not_found_elements = []
        for element in elements:
            how, what = element
            if not self.is_element_present(how, what):
                not_found_elements.append(what)
        if not_found_elements:
            assert False, f'Elements not found: {not_found_elements}'

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_not_elements_present(self, elements: tuple, timeout=4):
        found_elements = []
        for element in elements:
            how, what = element
            if not self.is_not_element_present(how, what):
                found_elements.append(what)
        if found_elements:
            assert False, f'Elements not found: {found_elements}'

    def open(self):
        self.browser.get(self.url)

    def open_url(self, link:str, flag=None):
        self.browser.get(link)
        if flag is not None:
            current_url = self.browser.current_url
            assert flag in current_url, f"{flag} is not in URL: {current_url}"

    def return_element_text(self, how, what):
        try:
            data = self.browser.find_element(how, what).text
        except:
            return False
        return data
