import os
import time

import allure
from selenium.webdriver.common.by import By

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import MainPageNoLoginNavbarLoc, MainPageNoLoginCarouselLoc, MainPageNoLoginCases, \
    MainPageNoLoginCookie, MainPageNoLoginEducate, MainPageNoLoginNews, MainPageNoLoginFooter


@allure.story("Header TestCase")
class TestHeader(BaseCaseVkAd):
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

    @allure.title("Aducation maouseover Test")
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



@allure.story("Carousel TestCase")
class TestСarousel(BaseCaseVkAd):
    authorize = False

    @allure.title("View carousel Test")
    def test_display_carousel(self):
        carousel = self.base_page.find(MainPageNoLoginCarouselLoc.CAROUSEL_CONTAINER)
        assert carousel.is_displayed(), "Карусель не отображается на странице"

    @allure.title("Carousel autoscroll Test")
    def test_carousel_autoscroll(self):
        self.base_page.click(MainPageNoLoginCarouselLoc.MAIN_PAGE_CAROUSEL_ROUND_BTN_1)
        container = self.base_page.find(MainPageNoLoginCarouselLoc.CAROUSEL_BULLETS_CONTAINER)
        firstBullet = container.find_element(By.TAG_NAME, 'DIV')
        initial_class = firstBullet.get_attribute('class')
        time.sleep(8)
        new_class = firstBullet.get_attribute('class')

        assert initial_class != new_class, "Не произошло автопереключение"

    @allure.title("Carousel switch Test")
    def test_carousel_switch(self):
        container = self.base_page.find(MainPageNoLoginCarouselLoc.CAROUSEL_BULLETS_CONTAINER)
        firstBullet = container.find_element(By.TAG_NAME, 'DIV')
        self.base_page.click(MainPageNoLoginCarouselLoc.MAIN_PAGE_CAROUSEL_ROUND_BTN_2)
        initial_class = firstBullet.get_attribute('class')

        self.base_page.click(MainPageNoLoginCarouselLoc.MAIN_PAGE_CAROUSEL_ROUND_BTN_1)
        new_class = firstBullet.get_attribute('class')

        assert initial_class != new_class, "Не сработало переключение"

    @allure.title("Carousel button handler Test")
    def test_carousel_button(self):
        current_window = self.driver.current_window_handle
        self.base_page.click(MainPageNoLoginCarouselLoc.MAIN_PAGE_CAROUSEL_ROUND_BTN_1)
        self.base_page.click(MainPageNoLoginCarouselLoc.CAROUSEL_HANDLE_BTN)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/promo/firstbonus',len('https://ads.vk.com/promo/firstbonus')), "Переход не произошел"

@allure.story("Cases TestCase")
class TestCases(BaseCaseVkAd):

    authorize = False
    @allure.title("Company cases view Test")
    def test_company_cases(self):
        cases = self.base_page.find(MainPageNoLoginCases.CASES_CONTAINER)
        header = cases.find_element(By.TAG_NAME, 'h2')
        cases_examples = cases.find_element(*MainPageNoLoginCases.CASES_EXAMPLES)
        href = cases.find_element(By.TAG_NAME, 'a')
        assert (header.text == 'Кейсы компаний' and cases_examples.is_displayed() and href.is_displayed() ), "Кейсы компаний не отображаются корректно"

    @allure.title("Transfer to company cases page Test")
    def test_company_cases_page(self):
        current_window = self.driver.current_window_handle
        self.base_page.click(MainPageNoLoginCases.CASES_HREF)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/cases',len('https://ads.vk.com/cases')), "Переход не произошел"

    @allure.title("Transfer to chosen case")
    def test_chosen_case(self):
        case = self.base_page.find(MainPageNoLoginCases.CHOSEN_CASE)
        title = case.find_element(*MainPageNoLoginCases.CASE_TITLE).text
        case.click()
        header = self.base_page.find(MainPageNoLoginCases.CASE_PAGE_TITLE)
        new_title = header.find_element(By.TAG_NAME, 'h1').text

        assert title == new_title, "Переход не на ту страницу"

@allure.story("Cookie Test")
class TestCookie(BaseCaseVkAd):

    authorize = False
    @allure.title("Cookie view Test")
    def test_cookie(self):
        cookie = self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)

        assert cookie.is_displayed(), 'Предупреждение о куки не отображается'

    @allure.title("Cookie view reload Test")
    def test_cookie_reload(self):
        cookie = self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)

        assert cookie.is_displayed(), 'Предупреждение о куки не отображается'

        self.driver.refresh()

        cookie = self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)

        assert cookie.is_displayed(), 'Предупреждение о куки не отображается'

    @allure.title("Cookie close Test")
    def test_cookie_close(self):
        cookie = self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
        cookie.find_element(By.TAG_NAME, 'button').click()

        try:
            self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
            assert False, "Предупреждение о куки всё ещё отображается"
        except:
            assert True

    @allure.title('Cookie close reload Test')
    def test_cookie_close_reload(self):
        cookie = self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
        cookie.find_element(By.TAG_NAME, 'button').click()

        try:
            self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
            assert False, "Предупреждение о куки всё ещё отображается"
        except:
            assert True

        self.driver.refresh()

        try:
            self.base_page.find(MainPageNoLoginCookie.COOKIE_CONTAINER)
            assert False, "Предупреждение о куки всё ещё отображается"
        except:
            assert True


@allure.story("Educate Test")
class TestEducate(BaseCaseVkAd):
    authorize = False

    @allure.title("Educate view Test")
    def test_educate(self):
        self.base_page.move_to_element(MainPageNoLoginEducate.EDUCATE_CONTAINER)
        educate = self.base_page.find(MainPageNoLoginEducate.EDUCATE_CONTAINER)

        assert educate.is_displayed(), "Блок не отображается"


    @allure.title("Educate more Test")
    def test_educate_more(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginEducate.EDUCATE_ABOUT)
        self.base_page.click(MainPageNoLoginEducate.EDUCATE_ABOUT)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/events',
                                            len('https://ads.vk.com/events')), "Переход не произошел"



    @allure.title("Educate click Test")
    def test_educate_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginEducate.EDUCATE_CONTAINER)
        educate = self.base_page.find(MainPageNoLoginEducate.EDUCATE_CONTAINER)
        educate.click()
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/events',
                                            len('https://ads.vk.com/events')), "Переход не произошел"

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

@allure.story("Footer Test")
class TestFooter(BaseCaseVkAd):
    authorize = False
    @allure.title("Footer view Test")
    def test_footer(self):
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_CONTAINER)
        footer = self.base_page.find(MainPageNoLoginFooter.FOOTER_CONTAINER)

        assert footer.is_displayed(), 'Footer не отображается'

    @allure.title("Footer logo view Test")
    def test_footer_logo(self):
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_CONTAINER)
        footer = self.base_page.find(MainPageNoLoginFooter.FOOTER_CONTAINER)
        logo = footer.find_element(*MainPageNoLoginFooter.FOOTER_LOGO)
        svg_element = logo.find_element(By.TAG_NAME, 'svg')
        xmlns_attribute = svg_element.get_attribute('xmlns')
        assert xmlns_attribute == 'http://www.w3.org/2000/svg', "Атрибут xmlns не совпадает"

    @allure.title("Footer logo click Test")
    def test_footer_click(self):
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_LOGO)
        self.base_page.click(MainPageNoLoginFooter.FOOTER_LOGO, 5)
        assert self.base_page.is_opened('https://ads.vk.com/'), "Переход на главную страницу не произошел"

    @allure.title("Footer transfer to account Test")
    def test_footer_to_account(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_CONTAINER)
        footer = self.base_page.find(MainPageNoLoginFooter.FOOTER_CONTAINER)
        footer.find_element(*MainPageNoLoginFooter.TO_ACCOUNT).click()
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://id.vk.com/auth',len('https://id.vk.com/auth')), "Переход на страницу авторизации не произошел"

    @allure.title("Footer sections view Test")
    def test_footer_sections(self):
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_CONTAINER)
        assert self.base_page.find(MainPageNoLoginFooter.FOOTER_SECTIONS).is_displayed(), "Разделы не отображаются"

        sections = self.driver.find_elements(*MainPageNoLoginFooter.FOOTER_SECTIONS_LI)
        actual_count = len(sections)

        assert actual_count == 8, "В разделе не 8 элементов"

    @allure.title("News tranfer test")
    def test_news_transfer(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_NEWS)
        self.base_page.click(MainPageNoLoginFooter.FOOTER_NEWS)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/news',len('https://ads.vk.com/news')), "Переход на страницу новости не произошел"

    @allure.title("Useful materials tranfer test")
    def test_news_transfer(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_MATERIALS)
        self.base_page.click(MainPageNoLoginFooter.FOOTER_MATERIALS)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/insights',
                                            len('https://ads.vk.com/insights')), "Переход на страницу материалов не произошел"

    @allure.title("Documents tranfer test")
    def test_documents_transfer(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_DOCUMENTS)
        self.base_page.click(MainPageNoLoginFooter.FOOTER_DOCUMENTS)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/documents',
                                            len('https://ads.vk.com/documents')), "Переход на страницу документов не произошел"

    @allure.title("VK logo view test")
    def test_vk_logo_view(self):
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_VK_LOGO)

        assert self.base_page.find(MainPageNoLoginFooter.FOOTER_VK_LOGO).is_displayed(), "Лого ВК не отображается"

    @allure.title("VK logo click test")
    def test_vk_logo_click(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_VK_LOGO)
        self.base_page.click(MainPageNoLoginFooter.FOOTER_VK_LOGO)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://vk.company/ru/company/business/',
                                            len('https://vk.company/ru/company/business/')), "Переход на страницу бизнеса не произошел"

    @allure.title("SocialNetworks view test")
    def test_social_networks_view(self):
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_SOCIAL)

        assert self.base_page.find(MainPageNoLoginFooter.FOOTER_SOCIAL).is_displayed(), "Ссылки на соцсети не отображается"

    @allure.title("Switch language view test")
    def test_switch_language_view(self):
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_LANGUAGES)
        self.base_page.click(MainPageNoLoginFooter.FOOTER_LANGUAGES)
        assert self.base_page.find(MainPageNoLoginFooter.FOOTER_CHOOSE_LANGUAGES).is_displayed(), "Не отображаются языки"

    @allure.title("Switch language test")
    def test_switch_language_view(self):
        current_window = self.driver.current_window_handle
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_LANGUAGES)
        self.base_page.click(MainPageNoLoginFooter.FOOTER_LANGUAGES)
        self.base_page.click(MainPageNoLoginFooter.FOOTER_CHOOSE_ENGLISH)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/en',
                                            len('https://ads.vk.com/en')), "Переход на страницу англоязычную не произошел"


    @allure.title("Switch languages mouseover test")
    def test_switch_language_mouseover(self):
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_LANGUAGES)
        self.base_page.click(MainPageNoLoginFooter.FOOTER_LANGUAGES)
        self.base_page.move_to_element(MainPageNoLoginFooter.FOOTER_CHOOSE_ENGLISH)
        self.base_page.move_to_element(MainPageNoLoginFooter.TO_ACCOUNT)

        assert self.base_page.is_element_not_present(MainPageNoLoginFooter.FOOTER_CHOOSE_LANGUAGES), "Выбор до сих пор отображается"
