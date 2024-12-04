import os
import time

import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import AuthLocators

@allure.story("Авторизация и проверка профиля")
class TestLogin(BaseCaseVkAd):
    authorize = True
    @allure.title("Проверка авторизации")
    def test_login(self):
        fio = self.base_page.get_text(AuthLocators.SURNAME_NAME_DIV_MAXORELLA, 20)
        self.save_cookies('cookies.json')
        assert fio == self.profile_fi, f"Ожидалось: '{self.profile_fi}', но было получено: '{fio}'"
