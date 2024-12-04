import allure
from selenium.webdriver.common.by import By

from hw.code.asserts.asserts import attribute_assert, assert_is_page_open, assert_compare_block_text, find_assert
from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import MainPageNoLoginNavbarLoc


@allure.story("Navigation TestCase")
class TestNavigation(BaseCaseVkAd):
    authorize = False

    @allure.title("View Logo Test")
    def test_logo(self):
        logo = self.base_page.find(MainPageNoLoginNavbarLoc.MAIN_PAGE_LOGO_BTN)
        svg_element = logo.find_element(By.TAG_NAME,'svg')
        xmlns_attribute = svg_element.get_attribute('xmlns')
        assert xmlns_attribute == 'http://www.w3.org/2000/svg', "Атрибут xmlns не совпадает"

    @allure.title("Logo Click Test")
    def test_logo_click(self):
        assert_is_page_open(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_LOGO_BTN, 'https://ads.vk.com/',
                            message="Переход на главную страницу не произошел")

    @allure.title("Navigation View Test")
    def test_display_navbar(self):

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_HEADER_NEWS_BTN,
                                  'Новости', message= "Текст новости в Navbar не совпадает")

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_ADUCATION,
                                  'Обучение', message="Текст Обучение в Navbar не совпадает")

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_CASES_BTN,
                                  'Кейсы', message="Текст Кейсы в Navbar не совпадает")

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_IDEAS_BTN,
                                  'Форум идей', message="Текст Форум идей в Navbar не совпадает")

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_MONETIZATION_BTN,
                                  'Монетизация', message="Текст Монетизация в Navbar не совпадает")

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_REFERENCE_BTN,
                                  'Справка', message="Текст Справка в Navbar не совпадает")

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_GO_TO_LK_BTN,
                                  'Перейти в кабинет', message="Текст Перейти в кабинет в Navbar не совпадает")

    @allure.title("News click Test")
    def test_news_click(self):
        assert_is_page_open(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_HEADER_NEWS_BTN, 'https://ads.vk.com/news',
                            message="Переход на новостную страницу не произошел")

    @allure.title("Cases click Test")
    def test_cases_click(self):
        assert_is_page_open(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_CASES_BTN,
                            'https://ads.vk.com/cases',
                            message="Переход на кейс страницу не произошел")

    @allure.title("Upvote click Test")
    def test_upvote_click(self):
        assert_is_page_open(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_IDEAS_BTN,
                            'https://ads.vk.com/upvote',
                            message="Переход на форум идей страницу не произошел")

    @allure.title("Partner click Test")
    def test_partner_click(self):
        assert_is_page_open(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_MONETIZATION_BTN, 'https://ads.vk.com/partner',
                            message="Переход на партнерскую страницу не произошел")

    @allure.title("Help click Test")
    def test_help_click(self):
        assert_is_page_open(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_REFERENCE_BTN,
                            'https://ads.vk.com/help',
                            message="Переход на страницу помощи не произошел")

    @allure.title("Education popup Test")
    def test_open_study(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_USEFUL_MATERIALS_BTN,
                                  'Полезные материалы', message="Текст полезные материалы в Popup не совпадает")

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_EVENTS_BTN,
                                  'Мероприятия', message="Текст Мероприятия в Popup не совпадает")

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_VIDEOCOURSES_BTN,
                                  'Видеокурсы', message="Текст Видеокурсы в Popup не совпадает")

        assert_compare_block_text(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_CERRTIFICATES_BTN,
                                  'Сертификация', message="Текст Сертификация в Popup не совпадает")

    @allure.title("Useful materials click Test")
    def test_materials_click(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        assert_is_page_open(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_USEFUL_MATERIALS_BTN,
                            'https://ads.vk.com/insights',
                            message="Переход на страницу материалов не произошел")

    @allure.title("Events click Test")
    def test_events_click(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        assert_is_page_open(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_EVENTS_BTN,
                            'https://ads.vk.com/events',
                            message="Переход на страницу мероприятий не произошел")

    @allure.title("Video courses click Test")
    def test_courses_click(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        assert_is_page_open(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_VIDEOCOURSES_BTN,
                            'https://ads.vk.com/catalog/courses/',
                            message="Переход на страницу видеокурсы не произошел")

    @allure.title("Certificates click Test")
    def test_certification_click(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)

        assert_is_page_open(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_CERRTIFICATES_BTN,
                            'https://ads.vk.com/certification/',
                            message="Переход на страницу сертификатов не произошел")

    @allure.title("Education mouseover Test")
    def test_close_study(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.MAIN_PAGE_LOGO_BTN)

        find_assert(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_USEFUL_MATERIALS_BTN,
                    message="Меню отображается, но не должно!")
        find_assert(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_EVENTS_BTN,
                    message="Меню отображается, но не должно!")
        find_assert(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_VIDEOCOURSES_BTN,
                    message="Меню отображается, но не должно!")
        find_assert(self.base_page, MainPageNoLoginNavbarLoc.MAIN_PAGE_CERRTIFICATES_BTN,
                    message="Меню отображается, но не должно!")

    @allure.title("Transfer to account Test")
    def test_auth_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_GO_TO_LK_BTN, 5)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://id.vk.com/auth',len('https://id.vk.com/auth')), "Переход на страницу авторизации не произошел"
