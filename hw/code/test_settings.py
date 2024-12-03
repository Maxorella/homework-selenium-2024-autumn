import time

import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_settings_locators import SettingsLocators


@allure.story("Settings TestCase")
class TestSettings(BaseCaseVkAd):
    authorize = True

    @allure.title("Settings 1 Test")
    def test_settings_1(self):
        self.base_page.click(SettingsLocators.SETTINGS_BTN,20)
        assert self.base_page.is_opened('https://ads.vk.com/hq/settings'), "Переход на настройки не произошел"


    @allure.title("Settings 2 Test")
    def test_settings_2(self):
        self.base_page.click(SettingsLocators.SETTINGS_BTN,20)
        assert self.base_page.is_opened('https://ads.vk.com/hq/settings'), "Переход на настройки не произошел"

        text = self.base_page.get_text(SettingsLocators.TELE_TEXT, 5)
        assert text == 'Телефон', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.EMAIL_TEXT, 5)
        assert text == 'Email', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.EMAIL_LINK, 5)
        assert text == 'Добавить email', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.FIO_LINK, 5)
        assert text == 'ФИО', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.INN_LINK, 5)
        assert text == 'ИНН', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.NAZB_CAB, 5)
        assert text == 'Название кабинета', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.LANG_INT, 5)
        assert text == 'Язык интерфейса', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.SVYAZ_CAB, 5)
        assert text == 'Связанные кабинеты', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.EXIT_OTHER_USTR, 5)
        assert text == 'Выйти из других устройств', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.DELETE_CAB_BTN, 5)
        assert text == 'Удалить кабинет', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"


    @allure.title("Settings 3 Test")
    def test_settings_3(self):
        self.base_page.click(SettingsLocators.SETTINGS_BTN,20)
        assert self.base_page.is_opened('https://ads.vk.com/hq/settings'), "Переход на настройки не произошел"

        self.base_page.click(SettingsLocators.UVEDOML_BTN,20)

        text = self.base_page.get_text(SettingsLocators.UVEDOML_BTN, 15)
        assert text == 'Уведомления', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.SPOS_POLUCH, 15)
        assert text == 'Способы получения', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.MESS_TELEG, 15)
        assert text == 'Сообщение в Telegram', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.OSNOVN, 15)
        assert text == 'Основные', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.NEWS_DISC, 15)
        assert text == 'Новости и акции', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"



    @allure.title("Settings 4 Test")
    def test_settings_4(self):
        self.base_page.click(SettingsLocators.SETTINGS_BTN,20)
        assert self.base_page.is_opened('https://ads.vk.com/hq/settings'), "Переход на настройки не произошел"

        self.base_page.click(SettingsLocators.PRAVA_BTN_MENU,20)
        assert self.base_page.is_opened('https://ads.vk.com/hq/settings/access'), "Переход на Права доступа не произошел"


        text = self.base_page.get_text(SettingsLocators.PRAVA_BTN_MENU, 15)
        assert text == 'Права доступа', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.ADD_CAB_BTN_TEXT, 15)
        assert text == 'Добавить кабинет', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"

        text = self.base_page.get_text(SettingsLocators.PODROBN_TEXT, 15)
        assert text == 'Подробнее', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"


    @allure.title("Settings 5 Test")
    def test_settings_5(self):
        self.base_page.click(SettingsLocators.SETTINGS_BTN,20)
        assert self.base_page.is_opened('https://ads.vk.com/hq/settings'), "Переход на настройки не произошел"

        self.base_page.click(SettingsLocators.HIST_BTN_MENU,20)
        assert self.base_page.is_opened('https://ads.vk.com/hq/settings/logs'), "Переход на История изменений не произошел"

        text = self.base_page.get_text(SettingsLocators.HIST_TAB_TEXT, 15)
        assert text == 'Здесь будет храниться история изменений в кабинете', f"Ожидалось: 'длинный текст, см код..', но было получено: '{text}'"