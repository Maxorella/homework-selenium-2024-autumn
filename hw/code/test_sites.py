import time

import allure

from hw.code.asserts.asserts import *
from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_sites_locators import SitesLocators


@allure.story("Sites TestCase")
class TestSites(BaseCaseVkAd):
    authorize = True

    @allure.title("Test open 'Сайты' page")
    def test_sites_1(self):

        assert_is_page_open(self.base_page, SitesLocators.GO_TO_SITES_BTN, 'https://ads.vk.com/hq/pixels', 10,  "Переход на аудитории не произошел")


    @allure.title("Test display, buttons Add pixel and fields for image search.")
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


    @allure.title("click on the 'Add Pixel' button")
    def test_sites_3(self):
        assert_is_page_open(self.base_page, SitesLocators.GO_TO_SITES_BTN, 'https://ads.vk.com/hq/pixels',
                            20, "Переход на аудитории не произошел")

        self.base_page.click(SitesLocators.ADD_PIX_MENU_BTN,10)

    @allure.title("Adding a pixel. Enter the site domain. If an incorrect domain is entered, an error appears.")
    def test_sites_4(self):
        assert_is_page_open(self.base_page, SitesLocators.GO_TO_SITES_BTN, 'https://ads.vk.com/hq/pixels',
                            20, "Переход на аудитории не произошел")

        self.base_page.click(SitesLocators.ADD_PIX_MENU_BTN, 20)