import pytest

import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import json

from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.cases_page import CasesPage
from hw.code.ui.pages.events_page import EventsPage
from hw.code.ui.pages.materials_page import MaterialsPage
from hw.code.ui.pages.news_page import NewsPage

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

@pytest.fixture(scope='function')
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
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()

@pytest.fixture
def base_vk_ad_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def news_vk_ad_page(driver):
    return NewsPage(driver=driver)

@pytest.fixture
def materials_vk_ad_page(driver):
    return MaterialsPage(driver=driver)

@pytest.fixture
def events_vk_ad_page(driver):
    return EventsPage(driver=driver)

@pytest.fixture
def cases_vk_ad_page(driver):
    return CasesPage(driver=driver)

@pytest.fixture(scope='session')
def credentials_vk_ad():
    email = os.getenv('email')
    password = os.getenv('password')
    profile_fi = os.getenv('profile_fi')

    return {
        'email':      email,
        'password':   password,
        'profile_fi': profile_fi
    }

@pytest.fixture(scope='session')
def user_to_find_vked():
    with open('files/userdata.json', 'r') as f:
        userdata = json.load(f)

    name_to_find = userdata['name_to_find']
    surname_to_find = userdata['surname_to_find']
    return {
        'name_to_find':      name_to_find,
        'surname_to_find':   surname_to_find,
    }

COOKIE_FILE = 'cookies.json'

@pytest.fixture(scope='session')
def save_cookies(driver):
    yield
    with open(COOKIE_FILE, 'w') as file:
        cookies = driver.get_cookies()
        json.dump(cookies, file)

@pytest.fixture(scope='function')
def load_cookies(driver):
    driver.get('https://example.com')
    try:
        with open(COOKIE_FILE, 'r') as file:
            cookies = json.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        driver.refresh()
    except FileNotFoundError:
        print("Файл с куки не найден, выполняется тест без предварительных куки.")
