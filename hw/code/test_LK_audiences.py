import os
import time
from datetime import date

import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_audiences_locators import AudiencesLocators

@allure.story("Авторизация и проверка профиля")
class TestAudiences(BaseCaseVkAd):
    authorize = True

    @allure.title("1 Личный кабинет")
    def test_audience_click(self):
        self.base_page.click(AudiencesLocators.GO_AUDIENCES_BTN, 10)
        assert self.base_page.is_opened('https://ads.vk.com/hq/audience'), "Переход на аудитории не произошел"

    @allure.title("2 Аудитории")
    def test_audience_visibility(self):
        self.base_page.click(AudiencesLocators.GO_AUDIENCES_BTN, 15)
        assert self.base_page.is_opened('https://ads.vk.com/hq/audience'), "Переход на аудитории не произошел"

        assert self.base_page.element_presented(AudiencesLocators.UP_MENU_AUDIENCES_BTN, 20), "up menu не отображается"
        assert self.base_page.element_presented(AudiencesLocators.UP_MENU_USER_LIST_BTN, 5), "up menu не отображается"
        assert self.base_page.element_presented(AudiencesLocators.UP_MENU_OFFLINE_CONVERSION_BTN, 5), "up menu не отображается"

        assert self.base_page.element_presented(AudiencesLocators.UP_MENU_CREATE_AUDIENCE_BTN, 5), "не отображается"
        assert self.base_page.element_presented(AudiencesLocators.TRI_TOCH, 5), "не отображается"
        assert self.base_page.element_presented(AudiencesLocators.FILTER_TEXT, 5), "не отображается"
        assert self.base_page.element_presented(AudiencesLocators.SHARE_BTN, 5), "не отображается"
        assert self.base_page.element_presented(AudiencesLocators.DELETE_BTN, 5), "не отображается"
        assert self.base_page.element_presented(AudiencesLocators.SEARCH_FIELD, 5), "не отображается"


        text = self.base_page.get_text(AudiencesLocators.UP_MENU_CREATE_AUDIENCE_BTN, 5)
        assert text == 'Создать аудиторию', f"Ожидалось: 'Создать аудиторию', но было получено: '{text}'"

        text = self.base_page.get_text(AudiencesLocators.FILTER_TEXT, 5)
        assert text == 'Фильтр', f"Ожидалось: 'Фильтр', но было получено: '{text}'"

    @allure.title("3 Аудитории")
    def test_audience_create_click(self):
        self.base_page.click(AudiencesLocators.GO_AUDIENCES_BTN, 20)
        assert self.base_page.is_opened('https://ads.vk.com/hq/audience'), "Переход на аудитории не произошел"

        self.base_page.click(AudiencesLocators.UP_MENU_CREATE_AUDIENCE_BTN, 20)

        text = self.base_page.get_text(AudiencesLocators.CREATE_AUDIENCE_TEXT, 20)
        assert text == 'Создание аудитории', f"Ожидалось: 'Создание аудитории', но было получено: '{text}'"


    @allure.title("4 Создание аудитории")
    def test_audience_create_pipe(self):
        self.base_page.click(AudiencesLocators.GO_AUDIENCES_BTN, 20)
        assert self.base_page.is_opened('https://ads.vk.com/hq/audience'), "Переход на аудитории не произошел"
        self.base_page.click(AudiencesLocators.UP_MENU_CREATE_AUDIENCE_BTN, 20)

        text = self.base_page.get_text(AudiencesLocators.CREATE_AUDIENCE_TEXT, 5)
        assert text == 'Создание аудитории', f"Ожидалось: 'Создание аудитории', но было получено: '{text}'"
        text_16 = "GOOD NAME 16 CHA"
        text_256 = text_16 * 16

        self.base_page.enter_field(AudiencesLocators.NAME_AUDIENCE_INPUT, text_256, 10)

        text = self.base_page.get_text(AudiencesLocators.NAME_AUDIENCE_ERROR_TEXT, 5)
        assert text == 'Напишите текст не больше 255 символов', f"Ожидалось: 'что-то', но было получено: '{text}'"

        self.base_page.enter_field(AudiencesLocators.NAME_AUDIENCE_INPUT, text_16, 10)
        self.base_page.click(AudiencesLocators.ADD_IST_BTN, 10)
        self.base_page.click(AudiencesLocators.SOOBS_SUBSC_BTN, 10)
        text_no_audie = "awfpodijaseofnewro_gneweawdawdawdadweawde"
        self.base_page.enter_field(AudiencesLocators.SEARCH_FIELD_SOOBS, text_no_audie, 10)

        text = self.base_page.get_text(AudiencesLocators.NOTH_FOUND_TEXT, 20)
        assert text == 'Ничего не нашлось', f"Ожидалось: 'что-то', но было получено: '{text}'"

    @allure.title("6 Создание аудитории")
    def test_audience_6(self):
        self.base_page.click(AudiencesLocators.GO_AUDIENCES_BTN, 20)
        assert self.base_page.is_opened('https://ads.vk.com/hq/audience'), "Переход на аудитории не произошел"
        self.base_page.click(AudiencesLocators.UP_MENU_CREATE_AUDIENCE_BTN, 20)

        text = self.base_page.get_text(AudiencesLocators.CREATE_AUDIENCE_TEXT, 5)
        assert text == 'Создание аудитории', f"Ожидалось: 'Создание аудитории', но было получено: '{text}'"

        today = date.today()
        text_aud = f"Аудитория {today}"

        self.base_page.click(AudiencesLocators.ADD_IST_BTN, 10)
        self.base_page.click(AudiencesLocators.SOOBS_SUBSC_BTN, 10)

        text_lmao = "lmao"
        self.base_page.enter_field(AudiencesLocators.SEARCH_FIELD_SOOBS, text_lmao, 10)

        self.base_page.click(AudiencesLocators.SELECT_ALL_BTN, 20)

        self.base_page.click(AudiencesLocators.Subsc_title_text, 20)
        self.base_page.click(AudiencesLocators.SAVE_BTN, 20)
        time.sleep(1) # антипаттерн, но так надо...
        self.base_page.click(AudiencesLocators.SAVE2_BTN, 20)


        title = self.base_page.get_text(AudiencesLocators.AUD_CREATED_TEXT, 20)
        assert title == text_aud, f"Ожидалось: 'Создание аудитории', но было получено: '{title}'"

