import re
import time
from .locators import LoginPageLocators
from pages.data import DATA
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


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

    def click_active_element(self, element, flag=None, timeout=15):
        try:
            count_of_tabs = len(self.browser.window_handles)
            link = self.browser.find_element(*element)
            link.click()
            if flag is not None:
                if len(self.browser.window_handles) > count_of_tabs:
                    old_tab = self.browser.window_handles[count_of_tabs-1]
                    new_tab = self.browser.window_handles[count_of_tabs]
                    self.browser.switch_to.window(new_tab)
                    WebDriverWait(self.browser, timeout, 3, TimeoutException).until(EC.url_contains((flag)))
                    current_url = self.browser.current_url
                    self.browser.close()
                    self.browser.switch_to.window(old_tab)
                else:
                    WebDriverWait(self.browser, timeout, 3, TimeoutException).until(EC.url_contains((flag)))
                    current_url = self.browser.current_url
                assert flag in current_url, f"{flag} is not in URL: {current_url}"
        except:
            return False
        return True

    def click_active_elements(self, elements: dict):
        problem_elements = []
        for element in elements:
            flag = elements[element]
            if not self.click_active_element(element, flag):
                problem_elements.append(flag)
            self.browser.back()
        if problem_elements:
            assert False, f'Check links does not have parts: {problem_elements}'

    def is_disappeared(self, element, timeout=4):
        how, what = element
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, element):
        try:
            self.browser.find_element(*element)
        except:
            return False
        return True

    def is_elements_present(self, elements: tuple):
        not_found_elements = []
        for element in elements:
            how, what = element
            if not self.is_element_present(element):
                not_found_elements.append(what)
        if not_found_elements:
            assert False, f'Elements not found: {not_found_elements}'

    def is_not_element_present(self, element, timeout=4):
        how, what = element
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_not_elements_present(self, elements: tuple, timeout=4):
        found_elements = []
        for element in elements:
            how, what = element
            if not self.is_not_element_present(element):
                found_elements.append(what)
        if found_elements:
            assert False, f'Elements not found: {found_elements}'

    def login(self, email=DATA['email'], password=DATA['password']):
        self.browser.get(self.url)
        self.text_input(LoginPageLocators.EMAIL_FIELD, email)
        self.text_input(LoginPageLocators.PASSWORD_FIELD, password)
        return self.click_active_element(LoginPageLocators.SIGNIN_BUTTON, 'feed')

    def open(self):
        self.browser.get(self.url)

    def open_url(self, link:str, flag=None):
        self.browser.get(link)
        if flag is not None:
            current_url = self.browser.current_url
            assert flag in current_url, f"{flag} is not in URL: {current_url}"

    def return_element_text(self, element):
        try:
            data = self.browser.find_element(*element).text
        except:
            return False
        return data

    def text_input(self, element, text: str):
        try:
            self.browser.find_element(*element).send_keys(text)
        except:
            assert False, f"Element: [{element}] doesn't accept text: [{text}]"

    def text_match(self, elements: tuple):
        expected_text, actual_text = elements
        return bool(re.search(expected_text, actual_text))
