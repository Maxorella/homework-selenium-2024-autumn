import time

import allure

from hw.code.news_case_vk import NewsCaseVkAd


@allure.story("News page")
class TestNewsCaseVkAd(NewsCaseVkAd):
    @allure.title("News page")
    def test_news_page(self):
        time.sleep(5)
