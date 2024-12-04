import allure
from selenium.webdriver.common.by import By

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import MainPageNoLoginFooter


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
