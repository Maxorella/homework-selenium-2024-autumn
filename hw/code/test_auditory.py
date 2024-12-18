import time

import allure
from datetime import datetime

from hw.code.base_case import BaseCase


@allure.story("Проверка Аудиторий")
class TestAuditory(BaseCase):

    # 1 тест
    @allure.title("Проверка создания аудитории по ключевой фразе")
    def test_create_auditory_phrase(self, auditory_page):
        auditory_page.find_create_aud_btn()
        auditory_page.click_create_auditory()

        auditory_page.find_add_ist_btn()
        auditory_page.click_add_ist_btn()

        auditory_page.find_phrases_btn()
        auditory_page.click_phrases_btn()

        auditory_page.find_create_phrase_window_elements()
        auditory_page.enter_auditory_name("Phrases")
        auditory_page.enter_phrase("пиво")
        auditory_page.click_save_phrase_btn()

        auditory_page.find_save_aud_button()
        auditory_page.click_save_aud_btn()

        auditory_page.go_to_edit_page()
        auditory_page.find_edit_page_labels()
        auditory_page.assert_edit_titles("пиво", "Phrases")
        auditory_page.delete_auditory()


    def test_delete_auditory(self, auditory_page):
        auditory_page.delete_auditory()


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

