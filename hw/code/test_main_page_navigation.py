import allure
from selenium.webdriver.common.by import By

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
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_LOGO_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/'), "Переход на главную страницу не произошел"

    @allure.title("Navigation View Test")
    def test_display_navbar(self):

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_HEADER_NEWS_BTN)
        assert text == 'Новости', "Текст новости в Navbar не совпадает"

        text = self.base_page.get_text(MainPageNoLoginNavbarLoc.MAIN_PAGE_ADUCATION)
        assert text == 'Обучение', "Текст Обучение в Navbar не совпадает"

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

    @allure.title("News click Test")
    def test_news_click(self):
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_HEADER_NEWS_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/news'), "Переход на новостную страницу не произошел"

    @allure.title("Cases click Test")
    def test_cases_click(self):
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_CASES_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/cases'), "Переход на кейс страницу не произошел"

    @allure.title("Upvote click Test")
    def test_upvote_click(self):
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_IDEAS_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/upvote'), "Переход на форум идей страницу не произошел"

    @allure.title("Partner click Test")
    def test_partner_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_MONETIZATION_BTN, 5)
        with self.switch_to_window(current_window, True):
            assert self.base_page.is_opened('https://ads.vk.com/partner'), "Переход на партнерскую страницу не произошел"

    @allure.title("Help click Test")
    def test_help_click(self):
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_REFERENCE_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/help'), "Переход на страницу помощи не произошел"

    @allure.title("Education popup Test")
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

    @allure.title("Useful materials click Test")
    def test_materials_click(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_USEFUL_MATERIALS_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/insights'), "Переход на страницу материалов не произошел"

    @allure.title("Events click Test")
    def test_events_click(self):
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_EVENTS_BTN, 5)
        assert self.base_page.is_opened('https://ads.vk.com/events'), "Переход на страницу мероприятий не произошел"

    @allure.title("Video courses click Test")
    def test_courses_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_VIDEOCOURSES_BTN, 5)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://expert.vk.com/catalog/courses/'), \
                "Переход на страницу видеокурсы не произошел"

    @allure.title("Certificates click Test")
    def test_certification_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginNavbarLoc.STUDY_POPUP)
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_CERRTIFICATES_BTN, 5)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://expert.vk.com/certification/'), \
                "Переход на страницу сертификатов не произошел"

    @allure.title("Education mouseover Test")
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

    @allure.title("Transfer to account Test")
    def test_auth_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.click(MainPageNoLoginNavbarLoc.MAIN_PAGE_GO_TO_LK_BTN, 5)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://id.vk.com/auth',len('https://id.vk.com/auth')), "Переход на страницу авторизации не произошел"
