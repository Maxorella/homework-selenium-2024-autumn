import os
import time

import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from ui.locators.vk_ad_main_locators import AuthLocators

@allure.story("Авторизация и проверка профиля")
class TestLogin(BaseCaseVkAd):
    authorize = True

    @allure.title("Проверка авторизации")
    def test_login(self):
        fio = self.base_page.get_text(AuthLocators.SURNAME_NAME_DIV, 10)
        self.save_cookies('cookies.json')
        assert fio == self.profile_fi, f"Ожидалось: '{self.profile_fi}', но было получено: '{fio}'"


@allure.story("Авторизация и проверка профиля c cookie")
class TestLoginCookie(BaseCaseVkAd):
    authorize = False
    use_cookie = True

    @allure.title("Проверка авторизации  с куки")
    def test_login(self):
        fio = self.base_page.get_text(AuthLocators.SURNAME_NAME_DIV, 10)
        assert fio == self.profile_fi, f"Ожидалось: '{self.profile_fi}', но было получено: '{fio}'"

use_cookies = True