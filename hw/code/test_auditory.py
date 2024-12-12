import time

import allure
from datetime import datetime

from hw.code.base_case import BaseCase


@allure.story("Проверка Аудиторий")
class TestAuditory(BaseCase):

    @allure.title("Проверка создания аудитории")
    def test_create_auditory(self, auditory_page):
        auditory_page.click_create_auditory()
        #auditory_page.enter_auditory_name("")
        auditory_page.click_add_ist()
        auditory_page.click_add_soobs_subsc()
        auditory_page.click_add_as_list()
        auditory_page.click_soobs()
        auditory_page.enter_soobs_href("https://vk.com/reallydank")
        auditory_page.click_confr_add()
        auditory_page.click_close_krest()
        auditory_page.click_save()
        auditory_page.click_submit_create()
        auditory_page.refresh_page()
        auditory_page.assert_lmao_span(expected_title=f"Аудитория {datetime.now().strftime('%Y-%m-%d')}")

