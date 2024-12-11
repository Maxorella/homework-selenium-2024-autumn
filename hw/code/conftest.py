import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from hw.code.ui.pages.auth_page import AuthPage
from hw.code.ui.pages.base_page import BasePage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://ads.vk.com/')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
    }


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()

    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)

@pytest.fixture
def auth_data():
    return {
        "email": os.getenv("email"),
        "password": os.getenv("password")
    }

@pytest.fixture
def main_page(auth_page, auth_data):
    main_page = auth_page.login_mail(auth_data["email"], auth_data["password"])
    return main_page

@pytest.fixture
def pixel_page(auth_page, auth_data):
    pixel_page = auth_page.login_pixels(auth_data["email"], auth_data["password"])
    return pixel_page

@pytest.fixture
def auditory_page(auth_page, auth_data):
    auditory_page = auth_page.login_auditory(auth_data["email"], auth_data["password"])
    return auditory_page

@pytest.fixture
def companies_page(auth_page, auth_data):
    companies_page = auth_page.go_to_companies(auth_data["email"], auth_data["password"])
    return companies_page