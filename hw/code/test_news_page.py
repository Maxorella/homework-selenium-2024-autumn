import time

import allure
from selenium.webdriver.common.by import By

from hw.code.asserts.asserts import find_assert, assert_compare_block_text, attribute_assert, assert_click_try
from hw.code.news_case_vk import NewsCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import MainPageNoLoginCookie
from hw.code.ui.locators.vk_ad_news_locators import NewsLocators


@allure.story("News page")
class TestNewsCaseVkAd(NewsCaseVkAd):
    @allure.title("News view page")
    def test_news_page(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)

        find_assert(self.news_page, NewsLocators.NEWS_HEADER, message="Header not found")

    @allure.title("News Content first Test")
    def test_news_content_first_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        cookie = self.news_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
        cookie.find_element(By.TAG_NAME, 'button').click()
        self.news_page.move_to_element(NewsLocators.ABOUT_FIRST)
        title = self.news_page.get_text(NewsLocators.FIRST_TITLE)
        self.news_page.move_to_element(NewsLocators.ABOUT_FIRST)
        self.news_page.click(NewsLocators.ABOUT_FIRST)

        assert_compare_block_text(self.news_page, NewsLocators.NEWS_TITLE, title, message="Перешли не на ту страницу или не перешли")

    @allure.title("Paggination total view Test ")
    def test_pagg_total_view_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        find_assert(self.news_page, NewsLocators.NEWS_HEADER, message="Общее количество не отображается")

    @allure.title("Paggination current page test")
    def test_pagg_current_page_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)

        attribute_assert(self.news_page, NewsLocators.NEWS_CURRENT_PAGE, 'data-page', '1',
                         "Неправильно отображается текущая страница")

    @allure.title("Paggination click page 2 Test")
    def test_pagg_click_2_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        self.news_page.move_to_element(NewsLocators.NEWS_SECOND_PAGE)
        self.news_page.click(NewsLocators.NEWS_SECOND_PAGE)
        self.news_page.find(NewsLocators.NEWS_SECOND_PAGE)
        self.news_page.move_to_element(NewsLocators.NEWS_SECOND_PAGE)

        attribute_assert(self.news_page, NewsLocators.NEWS_CURRENT_PAGE, 'data-page', '2',
                         "Не происходит переход на другую страницу")

    # error
    @allure.title("paggination go left test")
    def test_pagg_left_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        self.news_page.move_to_element(NewsLocators.NEWS_SECOND_PAGE)
        self.news_page.click(NewsLocators.NEWS_SECOND_PAGE)
        self.news_page.find(NewsLocators.NEWS_SECOND_PAGE)
        self.news_page.find(NewsLocators.PREV_PAGE)
        self.news_page.move_to_element(NewsLocators.PREV_PAGE)
        self.news_page.click(NewsLocators.PREV_PAGE, 10)
        self.news_page.find(NewsLocators.NEWS_CURRENT_PAGE)
        self.news_page.move_to_element(NewsLocators.NEWS_CURRENT_PAGE)

        attribute_assert(self.news_page, NewsLocators.NEWS_CURRENT_PAGE, 'data-page', '1',
                         "Не работает переход на предыдущую страницу")


    @allure.title("paggination go left block test")
    def test_pagg_left_block_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        self.news_page.move_to_element(NewsLocators.PREV_PAGE)

        assert_click_try(self.news_page, NewsLocators.PREV_PAGE, "Переход не заблокирован")


    @allure.title("Paggination go right Test")
    def test_pagg_go_right_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        self.news_page.move_to_element(NewsLocators.NEXT_PAGE)
        self.news_page.click(NewsLocators.NEXT_PAGE)
        self.news_page.find(NewsLocators.NEWS_SECOND_PAGE)
        self.news_page.find(NewsLocators.NEWS_SECOND_PAGE)
        self.news_page.move_to_element(NewsLocators.NEWS_SECOND_PAGE)

        attribute_assert(self.news_page, NewsLocators.NEWS_CURRENT_PAGE, 'data-page', '2',
                         "Не переходит на следующую страницу")


    @allure.title("Paggiantion block previous page test")
    def test_pagg_previous_page_test(self):
        self.news_page.click(NewsLocators.CLOSE_NOTIFICATION)
        self.news_page.move_to_element(NewsLocators.LAST_PAGE)
        self.news_page.click(NewsLocators.LAST_PAGE)
        self.news_page.move_to_element(NewsLocators.NEXT_PAGE)

        assert_click_try(self.news_page, NewsLocators.NEXT_PAGE, "Переход не заблокирован")
