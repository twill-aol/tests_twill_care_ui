import pytest
from datetime import datetime
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options as CHRO
from selenium.webdriver.firefox.options import Options as FIRO


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang")
    parser.addoption('--url', action='store', default='https://care.stage-twill.health',
                     help="Choose Server")

@pytest.fixture(scope="module")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        options = CHRO()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FIRO()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()

@pytest.fixture(scope="session")
def main_url(request):
    url_flag = request.config.getoption("url")
    if url_flag in ('prod', 'Prod', 'PROD') or url_flag in 'https://care.twill.health/':
        URL = 'https://care.twill.health'
    elif url_flag in 'https://qa02.dev.kopa.com/':
        URL = 'https://qa02.dev.kopa.com'
        URL = 'https://care.twill.health'
    else:
        URL = 'https://care.stage-twill.health'
    yield URL

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == 'call' and rep.failed:
#         now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         browser.save_screenshot(f".\\Screenshots\\fail_{now}.png")
