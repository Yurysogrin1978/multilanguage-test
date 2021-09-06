import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Browser: chrome or firefox?")
    parser.addoption('--language', action='store', default=None, help="Preffered language: ..?")

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    users_language = request.config.getoption('language')
    if (browser_name == 'chrome'):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': users_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", users_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print("\nquit browser..")
    browser.quit()