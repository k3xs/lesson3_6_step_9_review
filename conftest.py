import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language: es or fr')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    if language == "es":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif language == 'fr':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    else:
        raise pytest.UsageError("--language should be es of fr...")
    yield browser
    print("\nquit browser..")
    browser.quit()