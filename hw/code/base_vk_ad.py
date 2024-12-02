import os
import time
from contextlib import contextmanager
import json
import pytest
from _pytest.fixtures import FixtureRequest

from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.news_page import NewsPage
from ui.locators.vk_ad_main_locators import AuthLocators

CLICK_RETRY = 3


class BaseCaseVkAd:
    authorize = True
    use_cookie = False
    driver = None

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)


    def configure_browser_window(self, width, height, x=0, y=0):
        self.driver.set_window_size(width, height)
        self.driver.set_window_position(x, y)

    def full_size_window(self):
        self.driver.maximize_window()

    def save_cookies(self, file_path):
        """Сохраняет куки из браузера в файл."""
        with open(file_path, 'w') as file:
            cookies = self.driver.get_cookies()
            json.dump(cookies, file)

    def load_cookies(self, file_path):
        with open(file_path, 'r') as file:
            cookies = json.load(file)  # Список куки
            for cookie in cookies:
                self.driver.add_cookie(cookie)  # Добавляем куки
                print(cookie)
        self.driver.get("https://ads.vk.com/hq/overview")

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = (request.getfixturevalue('base_vk_ad_page'))
        # self.news_page: NewsPage = (request.getfixturevalue('news_vk_ad_page'))
        self.email, self.password, self.profile_fi = (
            request.getfixturevalue('credentials_vk_ad').values()
        )
        if self.authorize:
            self.base_page.click(AuthLocators.GO_TO_LK_BTN, 15)
            self.base_page.click(AuthLocators.GO_WITH_EMAIL_BTN, 15)
            self.base_page.enter_field(AuthLocators.EMAIL_ENTER_FIELD, self.email, 15)
            self.base_page.click(AuthLocators.ENTER_BTN, 15)
            self.base_page.click(AuthLocators.ENTER_OTHER_WAY_BTN, 15)
            self.base_page.enter_field(AuthLocators.PASSWORD_ENTER_FIELD, self.password, 15)
            self.base_page.click(AuthLocators.ENTER_PASSWORD_BTN, 15)


        if self.use_cookie:
            self.load_cookies('cookies.json')
            self.base_page.wait(20)

