import allure

from hw.code.asserts.asserts import find_assert, assert_is_page_opened, assert_is_page_open
from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import MainPageNoLoginNews


@allure.story('News Test')
class TestNews(BaseCaseVkAd):
    authorize = False
    @allure.title("News view Test")
    def test_news(self):

        find_assert(self.base_page, MainPageNoLoginNews.NEWS_CONTAINER, message="Блок не отображается")


    @allure.title("News about Test")
    def test_news_about(self):
        self.base_page.move_to_element(MainPageNoLoginNews.NEWS_ABOUT)

        assert_is_page_open(self.base_page, MainPageNoLoginNews.NEWS_ABOUT, 'https://ads.vk.com/news/sbor-auditorii-po-reklamnym-sobytiyam',
                            message="Переход не произошел")

    @allure.title("News click Test")
    def test_news_click(self):
        self.base_page.move_to_element(MainPageNoLoginNews.NEWS_CONTAINER)
        assert_is_page_open(self.base_page, MainPageNoLoginNews.NEWS_CONTAINER,
                            'https://ads.vk.com/news/sbor-auditorii-po-reklamnym-sobytiyam',
                            message="Переход не произошел")
