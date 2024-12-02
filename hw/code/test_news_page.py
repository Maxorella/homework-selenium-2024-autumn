import allure

from hw.code.base_vk_ad import BaseCaseVkAd


@allure.story("News page")
class TestNewsPage(BaseCaseVkAd):
    @allure.title("News page")
    def test_news_page(self):
        pass
