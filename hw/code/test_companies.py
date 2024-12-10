import time

import allure

from hw.code.base_case import BaseCase


@allure.story("Проверка кампаний")
class TestEducation(BaseCase):

    @allure.title("")
    def test(self, companies_page):
        companies_page.create_new_company()
        time.sleep(2)

        pass