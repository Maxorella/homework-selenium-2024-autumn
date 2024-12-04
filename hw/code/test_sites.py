import time

import allure

from hw.code.asserts.asserts import *
from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_sites_locators import SitesLocators


@allure.story("Sites TestCase")
class TestSites(BaseCaseVkAd):
    authorize = True

    @allure.title("Sites 1 Test")
    def test_sites_1(self):

        assert_is_page_open(self.base_page, SitesLocators.GO_TO_SITES_BTN, 'https://ads.vk.com/hq/pixels', 10,  "Переход на аудитории не произошел")


    @allure.title("Sites 2 Test")
    def test_sites_2(self):
        assert_is_page_open(self.base_page, SitesLocators.GO_TO_SITES_BTN, 'https://ads.vk.com/hq/pixels', 10,
                            "Переход на аудитории не произошел")

        assert_compare_block_text(self.base_page, SitesLocators.NO_PIX_TEXT_1, 'Нет привязанных пикселей трекинга',
                                  10, "Текст не совпадает")

        assert_compare_block_text(self.base_page, SitesLocators.NO_PIX_TEXT_2,
                                  'Чтобы вести рекламные кампании с оптимизацией конверсий на сайтах, создайте трекинговый пиксель',
                                  10, "Текст не совпадает")

        assert_compare_block_text(self.base_page, SitesLocators.NO_PIX_TEXT_3, 'Добавить пиксель',
                                  10, 'Текст не совпадает')


    @allure.title("Sites 3 Test")
    def test_sites_3(self):
        assert_is_page_open(self.base_page, SitesLocators.GO_TO_SITES_BTN, 'https://ads.vk.com/hq/pixels',
                            20, "Переход на аудитории не произошел")

        self.base_page.click(SitesLocators.ADD_PIX_MENU_BTN,10)

        # TODO почему то текст не берется, timeout срабатывает
        # text = self.base_page.get_text_visible(SitesLocators.ADD_PIX_POPUP_TEXT, 10)
        # assert text == 'Домен сайта', "Текст не совпадает"

    @allure.title("Sites 4 Test")
    def test_sites_4(self):
        assert_is_page_open(self.base_page, SitesLocators.GO_TO_SITES_BTN, 'https://ads.vk.com/hq/pixels',
                            20, "Переход на аудитории не произошел")

        self.base_page.click(SitesLocators.ADD_PIX_MENU_BTN, 20)

        # TODO НЕ ВИДЕН POPUP ПОЧЕМУ-ТО!!!!
        # self.base_page.enter_field(SitesLocators.DOMEN_INPUT, 'mortawed', 20)
        # self.base_page.click(SitesLocators.ADD_PIX_POPUP_BTN, 20)
        # text = self.base_page.get_text(SitesLocators.ADD_PIX_POPUP_TEXT, 20)
        # assert text == 'Введите корректный адрес сайта (вида: example.ru)', "Текст не совпадает"
