import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import MainPageNoLoginNews


@allure.story('News Test')
class TestNews(BaseCaseVkAd):
    authorize = False
    @allure.title("News view Test")
    def test_news(self):

        news = self.base_page.find(MainPageNoLoginNews.NEWS_CONTAINER)

        assert news.is_displayed(), "Блок не отображается"

    @allure.title("News about Test")
    def test_news_about(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginNews.NEWS_ABOUT)
        self.base_page.click(MainPageNoLoginNews.NEWS_ABOUT)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/news/sbor-auditorii-po-reklamnym-sobytiyam',
                                            len('https://ads.vk.com/news/sbor-auditorii-po-reklamnym-sobytiyam')), "Переход не произошел"

    @allure.title("News click Test")
    def test_news_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginNews.NEWS_CONTAINER)
        self.base_page.click(MainPageNoLoginNews.NEWS_CONTAINER)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/news/sbor-auditorii-po-reklamnym-sobytiyam',
                                            len('https://ads.vk.com/news/sbor-auditorii-po-reklamnym-sobytiyam')), "Переход не произошел"
