import os
import time

import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from ui.locators.vk_ad_main_locators import MainPageNoLoginNavbarLoc

@allure.story("Header TestCase")
class TestHeader(BaseCaseVkAd):
    authorize = False
    @allure.title("Header Test 2")
    def test_logo_click(self):
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_LOGO_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/'), "Переход на главную страницу не произошел"

    @allure.title("Header Test 1 + 3")
    def test_display_navbar_click(self):

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_HEADER_NEWS_BTN)
        assert text == 'Новости', "Текст новости в Navbar не совпадает"

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_CASES_BTN)
        assert text == 'Кейсы', "Текст Кейсы в Navbar не совпадает"

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_IDEAS_BTN)
        assert text == 'Форум идей', "Текст Форум идей в Navbar не совпадает"

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_MONETIZATION_BTN)
        assert text == 'Монетизация', "Текст Кейсы в Navbar не совпадает"

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_REFERENCE_BTN)
        assert text == 'Справка', "Текст Справка в Navbar не совпадает"

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_GO_TO_LK_BTN)
        assert text == 'Перейти в кабинет', "Текст Перейти в кабинет в Navbar не совпадает"
    @allure.title("Header Test 4")
    def test_news_click(self):
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_HEADER_NEWS_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/news'), "Переход на новостную страницу не произошел"

    @allure.title("Header Test 5")
    def test_cases_click(self):
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_CASES_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/cases'), "Переход на кейс страницу не произошел"

    @allure.title("Header Test 6")
    def test_upvote_click(self):
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_IDEAS_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/upvote'), "Переход на форум идей страницу не произошел"

    @allure.title("Header Test 7")
    def test_partner_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_MONETIZATION_BTN, 5)
        with self.switch_to_window(current_window, True):
            assert self.base_page.is_opened('https://ads.vk.com/partner'), "Переход на партнерскую страницу не произошел"

    @allure.title("Header Test 8")
    def test_help_click(self):
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_REFERENCE_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/help'), "Переход на страницу помощи не произошел"

    @allure.title("Header Test 9")
    def test_open_study(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_USEFUL_MATERIALS_BTN)
        assert text == 'Полезные материалы', "Текст новости в Navbar не совпадает"

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_EVENTS_BTN)
        assert text == 'Мероприятия', "Текст Мероприятия в Navbar не совпадает"

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_VIDEOCOURSES_BTN)
        assert text == 'Видеокурсы', "Текст Видеокурсы в Navbar не совпадает"

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_CERRTIFICATES_BTN)
        assert text == 'Сертификация', "Текст Сертификация в Navbar не совпадает"

    @allure.title("Header Test 10")
    def test_materials_click(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_USEFUL_MATERIALS_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/insights'), "Переход на страницу материалов не произошел"

    @allure.title("Header Test 11")
    def test_events_click(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_EVENTS_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/events'), "Переход на страницу мероприятий не произошел"

    @allure.title("Header Test 12")
    def test_courses_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_VIDEOCOURSES_BTN, 5)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://expert.vk.com/catalog/courses/'), \
                "Переход на страницу видеокурсы не произошел"

    @allure.title("Header Test 13")
    def test_certification_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_CERRTIFICATES_BTN, 5)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://expert.vk.com/certification/'), \
                "Переход на страницу сертификатов не произошел"

    @allure.title("Header Test 14")
    def test_close_study(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.MAIN_PAGE_LOGO_BTN)

        assert self.base_page.is_element_not_present(MainPageNoLoginNavbarLoc.MAIN_PAGE_USEFUL_MATERIALS_BTN), \
            "Меню отображается, но не должно!"

        assert self.base_page.is_element_not_present(MainPageNoLoginNavbarLoc.MAIN_PAGE_EVENTS_BTN), \
            "Меню отображается, но не должно!"

        assert self.base_page.is_element_not_present(MainPageNoLoginNavbarLoc.MAIN_PAGE_VIDEOCOURSES_BTN), \
            "Меню отображается, но не должно!"

        assert self.base_page.is_element_not_present(MainPageNoLoginNavbarLoc.MAIN_PAGE_CERRTIFICATES_BTN), \
            "Меню отображается, но не должно!"

    @allure.title("Header Test 15")
    def test_auth_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_GO_TO_LK_BTN, 5)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://id.vk.com/auth',len('https://id.vk.com/auth')), "Переход на страницу авторизации не произошел"


