import time

import allure

from hw.code.asserts.asserts import *
from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_settings_locators import SettingsLocators


@allure.story("Settings TestCase")
class TestSettings(BaseCaseVkAd):
    authorize = True

    @allure.title("1 Личный кабинет")
    def test_settings_1(self):
        assert_is_page_open(self.base_page, SettingsLocators.SETTINGS_BTN, 'https://ads.vk.com/hq/settings', 20,
                            "Переход на настройки не произошел")


    @allure.title("2 Настройки. Общие.")
    def test_settings_2(self):
        assert_is_page_open(self.base_page, SettingsLocators.SETTINGS_BTN, 'https://ads.vk.com/hq/settings', 20,
                            "Переход на настройки не произошел")

        assert_compare_block_text(self.base_page, SettingsLocators.TELE_TEXT, 'Телефон',
                                  5, 'Текст не совпал, ожидалось Телефон')

        assert_compare_block_text(self.base_page, SettingsLocators.EMAIL_TEXT, 'Email',
                                  5, 'Текст не совпал, ожидалось Email')

        assert_compare_block_text(self.base_page, SettingsLocators.EMAIL_LINK, 'Добавить email',
                                  5, 'Текст не совпал, ожидалось Добавить email')

        assert_compare_block_text(self.base_page, SettingsLocators.FIO_LINK, 'ФИО',
                                  5, 'Текст не совпал, ожидалось ФИО')

        assert_compare_block_text(self.base_page, SettingsLocators.INN_LINK, 'ИНН',
                                  5, 'Текст не совпал, ожидалось ИНН')

        assert_compare_block_text(self.base_page, SettingsLocators.NAZB_CAB, 'Название кабинета',
                                  5, 'Текст не совпал, ожидалось Название кабинета')

        assert_compare_block_text(self.base_page, SettingsLocators.LANG_INT, 'Язык интерфейса',
                                  5, 'Текст не совпал, ожидалось Язык интерфейса')

        assert_compare_block_text(self.base_page, SettingsLocators.SVYAZ_CAB, 'Связанные кабинеты',
                                  5, 'Текст не совпал, ожидалось Связанные кабинеты')

        assert_compare_block_text(self.base_page, SettingsLocators.EXIT_OTHER_USTR, 'Выйти из других устройств',
                                  5, 'Текст не совпал, ожидалось Выйти из других устройств')

        assert_compare_block_text(self.base_page, SettingsLocators.DELETE_CAB_BTN, 'Удалить кабинет',
                                  5, 'Текст не совпал, ожидалось Удалить кабинет')


    @allure.title("3 Настройки. Уведомления.")
    def test_settings_3(self):
        assert_is_page_open(self.base_page, SettingsLocators.SETTINGS_BTN, 'https://ads.vk.com/hq/settings', 20,
                            "Переход на настройки не произошел")

        self.base_page.click(SettingsLocators.UVEDOML_BTN,20)

        assert_compare_block_text(self.base_page, SettingsLocators.UVEDOML_BTN, 'Уведомления',
                                  15, 'Текст не совпал, ожидалось Уведомления')

        assert_compare_block_text(self.base_page, SettingsLocators.SPOS_POLUCH, 'Способы получения',
                                  15, 'Текст не совпал, ожидалось Способы получения')

        assert_compare_block_text(self.base_page, SettingsLocators.MESS_TELEG, 'Сообщение в Telegram',
                                  15, 'Текст не совпал, ожидалось Сообщение в Telegram')

        assert_compare_block_text(self.base_page, SettingsLocators.OSNOVN, 'Основные',
                                  15, 'Текст не совпал, ожидалось Основные')

        assert_compare_block_text(self.base_page, SettingsLocators.NEWS_DISC, 'Новости и акции',
                                  15, 'Текст не совпал, ожидалось Новости и акции')



    @allure.title("4 Настройки. Права доступа.")
    def test_settings_4(self):
        assert_is_page_open(self.base_page, SettingsLocators.SETTINGS_BTN, 'https://ads.vk.com/hq/settings', 20,
                            "Переход на настройки не произошел")

        assert_is_page_open(self.base_page, SettingsLocators.PRAVA_BTN_MENU, 'https://ads.vk.com/hq/settings/access', 20,
                            "Переход на Права доступа не произошел")

        assert_compare_block_text(self.base_page, SettingsLocators.PRAVA_BTN_MENU, 'Права доступа',
                                  15, 'Текст не совпал, ожидалось Права доступа')

        assert_compare_block_text(self.base_page, SettingsLocators.ADD_CAB_BTN_TEXT, 'Добавить кабинет',
                                  15, 'Текст не совпал, ожидалось Добавить кабинет')

        assert_compare_block_text(self.base_page, SettingsLocators.PODROBN_TEXT, 'Подробнее',
                                  15, 'Текст не совпал, ожидалось Подробнее')


    @allure.title("5 Настройки. История изменений.")
    def test_settings_5(self):
        assert_is_page_open(self.base_page, SettingsLocators.SETTINGS_BTN, 'https://ads.vk.com/hq/settings', 20,
                            "Переход на настройки не произошел")

        assert_is_page_open(self.base_page, SettingsLocators.HIST_BTN_MENU, 'https://ads.vk.com/hq/settings/logs', 20,
                            "Переход на История изменений не произошел")

        assert_compare_block_text(self.base_page, SettingsLocators.HIST_TAB_TEXT, 'Здесь будет храниться история изменений в кабинете',
                                  15, 'Текст не совпал, ожидалось Здесь будет храниться история изменений в кабинете')