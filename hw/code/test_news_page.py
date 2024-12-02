import time

import allure

from hw.code.news_case_vk import NewsCaseVkAd
from hw.code.ui.locators.vk_ad_news_locators import NewsLocators


@allure.story("News page")
class TestNewsCaseVkAd(NewsCaseVkAd):
    @allure.title("News view page")
    def test_news_page(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        assert self.news_page.find(NewsLocators.NEWS_HEADER).is_displayed(), "Header not found"

    @allure.title("News Content first Test")
    def test_news_content_first_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        self.news_page.move_to_element(NewsLocators.ABOUT_FIRST)
        title = self.news_page.get_text(NewsLocators.FIRST_TITLE)
        self.news_page.click(NewsLocators.ABOUT_FIRST)
        new_text = self.news_page.get_text(NewsLocators.NEWS_TITLE)

        assert title == new_text, "Перешли не на ту страницу или не перешли"

    @allure.title("Paggination total view Test ")
    def test_pagg_total_view_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        assert self.news_page.find(NewsLocators.NEWS_TOTAL).is_displayed(), "Общее количество не отображается"

    @allure.title("Paggination current page test")
    def test_pagg_current_page_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        page = self.news_page.get_attribute(NewsLocators.NEWS_CURRENT_PAGE,'data-page')
        assert page == '1', "Неправильно отображается текущая странциа"

    @allure.title("Paggination click page 2 Test")
    def test_pagg_click_2_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        self.news_page.move_to_element(NewsLocators.NEWS_SECOND_PAGE)
        self.news_page.click(NewsLocators.NEWS_SECOND_PAGE)
        self.news_page.move_to_element(NewsLocators.NEWS_SECOND_PAGE)
        page = self.news_page.get_attribute(NewsLocators.NEWS_CURRENT_PAGE, 'data-page')
        assert page == '2', "Не происходит переход на другую страницу"

    @allure.title("Paggination go right Test")
    def test_pagg_go_right_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        self.news_page.move_to_element(NewsLocators.NEXT_PAGE)
        self.news_page.click(NewsLocators.NEXT_PAGE)
        self.news_page.move_to_element(NewsLocators.NEWS_SECOND_PAGE)
        page = self.news_page.get_attribute(NewsLocators.NEWS_CURRENT_PAGE, 'data-page')
        assert page == '2', 'Не переходит на следующую страницу'