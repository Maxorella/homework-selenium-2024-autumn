import time

import allure

from hw.code.base_case import BaseCase


@allure.story("Проверка кампаний")
class TestEducation(BaseCase):

    @allure.title("Тест валидной ссылки")
    def test(self, companies_page):
        companies_page.create_new_company()
        companies_page.create_site_advertise()
        companies_page.enter_field(companies_page.locators.SITE_HREF, "https://www.statista.com")
        companies_page.click(companies_page.locators.CREATE_SITE_ADVERTISE)
        assert companies_page.element_presented(companies_page.locators.BUDGET_FIELD, 5), "Не расскрылись поля"


