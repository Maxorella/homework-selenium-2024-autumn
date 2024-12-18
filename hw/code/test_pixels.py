import time

import allure

from hw.code.base_case import BaseCase


@allure.story("Проверка Сайтов")
class TestSites(BaseCase):

    # 1 тест
    @allure.title("Проверка создания пикселя")
    def test_create_pixel_correct(self, pixel_page):
        pixel_page.find_create_pix_btn()
        pixel_page.click_create_pix()

        pixel_page.find_url_field()
        pixel_page.find_pixel_add_btn()

        pixel_page.enter_pixel_name("tean.homes")
        pixel_page.click_create_window_pix()

        pixel_page.find_create_option_new_pix()
        pixel_page.click_create_option_new_pix()

        pixel_page.find_close_crest()
        pixel_page.click_close_created()

        pixel_page.find_created_url_inlist()
        pixel_page.assert_created_url("tean.homes")

    # 3 тест
    @allure.title("Проверка редактирования названия пикселя")
    def test_edit_pixel_name(self, pixel_page):
        pixel_page.find_3_point_and_move()
        pixel_page.click_3_point()

        pixel_page.find_edit_name_dropped()
        pixel_page.click_edit_name_dropped()

        pixel_page.find_new_name_input()
        pixel_page.find_submit_edit_btn()

        pixel_page.enter_new_title("New title")
        pixel_page.click_submit_edit_name()

        pixel_page.refresh_page()

        pixel_page.find_pix_title()
        pixel_page.assert_new_title("New title")

    # 9 тест
    @allure.title("Создание аудиторного тега")
    def test_create_tag(self, pixel_page):
        pixel_page.click_settings()
        pixel_page.click_aud_tags()
        pixel_page.click_create_tag()
        pixel_page.enter_tag_name("mytag_name") # here
        pixel_page.click_submit_create_tag()
        pixel_page.assert_created_auditory("mytag_name")

    # 2 тест
    @allure.title("Проверка удаления")
    def test_delete_pixel(self, pixel_page):
        pixel_page.click_3_point()
        pixel_page.click_delete_dropped()
        pixel_page.click_submit_delete()
        pixel_page.assert_deleted_pixel()
