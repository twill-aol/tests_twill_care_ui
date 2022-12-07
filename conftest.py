import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang")
    parser.addoption('--url', action='store', default='https://care.stage-twill.health',
                     help="Choose Server")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    url_flag = request.config.getoption("url")
    if url_flag in ('prod', 'Prod', 'PROD') or url_flag in 'https://care.twill.health/':
        URL = 'https://care.twill.health'
    elif url_flag in 'https://qa02.dev.kopa.com/':
        URL = 'https://qa02.dev.kopa.com'
        URL = 'https://care.twill.health'
    else:
        URL = 'https://care.stage-twill.health/'
    language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser, URL
    browser.quit()
