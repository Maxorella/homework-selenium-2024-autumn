import os
import time

import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from ui.locators.vk_ad_main_locators import MainPageNoLoginLocators

@allure.story("Header TestCase")
class TestHeader(BaseCaseVkAd):
    authorize = False
    @allure.title("Header Test 2")
    def test_logo_click(self):
        self.base_page.click(MainPageNoLoginLocators.MAIN_PAGE_LOGO_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/'), "Переход на главную страницу не произошел"

    @allure.title("Header Test 4")
    def test_news_click(self):
        self.base_page.click(MainPageNoLoginLocators.MAIN_PAGE_HEADER_NEWS_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/news'), "Переход на новостную страницу не произошел"

    @allure.title("Header Test 5")
    def test_cases_click(self):
        self.base_page.click(MainPageNoLoginLocators.MAIN_PAGE_CASES_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/cases'), "Переход на кейс страницу не произошел"

    @allure.title("Header Test 6")
    def test_upvote_click(self):
        self.base_page.click(MainPageNoLoginLocators.MAIN_PAGE_IDEAS_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/upvote'), "Переход на форум идей страницу не произошел"

    @allure.title("Header Test 7")
    def test_partner_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.click(MainPageNoLoginLocators.MAIN_PAGE_MONETIZATION_BTN, 5)
        with self.switch_to_window(current_window, True):
            assert self.base_page.is_opened('https://ads.vk.com/partner'), "Переход на партнерскую страницу не произошел"

    @allure.title("Header Test 8")
    def test_help_click(self):
        self.base_page.click(MainPageNoLoginLocators.MAIN_PAGE_REFERENCE_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/help'), "Переход на страницу помощи не произошел"
