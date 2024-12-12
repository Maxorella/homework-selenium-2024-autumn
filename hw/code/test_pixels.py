import time

import allure

from hw.code.base_case import BaseCase


@allure.story("Проверка Сайтов")
class TestSites(BaseCase):

    @allure.title("Проверка создания пикселя")
    def test_create_pixel_correct(self, pixel_page):
        pixel_page.click_create_pix()
        pixel_page.enter_pixel_name("tean.homes")
        pixel_page.click_create_window_pix()
        pixel_page.click_create_new_pix()
        pixel_page.click_close_created()
        pixel_page.assert_created_url("tean.homes")


    @allure.title("Создание аудиторного тега")
    def test_create_tag(self, pixel_page):
        pixel_page.click_settings()
        pixel_page.click_aud_tags()
        pixel_page.click_create_tag()
        pixel_page.enter_tag_name("mytag_name") # here
        pixel_page.click_submit_create_tag()
        pixel_page.assert_created_auditory("mytag_name")


    @allure.title("Проверка удаления")
    def test_delete_pixel(self, pixel_page):
        pixel_page.click_3_point()
        pixel_page.click_delete_dropped()
        pixel_page.click_submit_delete()
        pixel_page.assert_deleted_pixel()
