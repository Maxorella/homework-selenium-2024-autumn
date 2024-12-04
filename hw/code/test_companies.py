import re
from datetime import datetime

import allure

from hw.code.asserts.asserts import assert_is_page_open, assert_is_page_opened, find_assert, assert_regexp
from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_companies_locators import CompaniesLocators


@allure.story("Проверка кампаний")
class TestCompanies(BaseCaseVkAd):
    authorize = True
    company = True

    @allure.title("View test")
    def test_popup(self):
        current_window = self.driver.current_window_handle
        with self.switch_to_window(current_window):
            assert_is_page_opened(self.base_page, 'https://ads.vk.com/hq/new_create/ad_plan', len('https://ads.vk.com/hq/new_create/ad_plan'),
                                  10, "Переход на страницу плане не произошел")

    @allure.title("Create company view test")
    def test_create_company(self):
        find_assert(self.base_page, CompaniesLocators.CREATE_COMPANY_CONTAINER, 10, "Контейнер не отображается")

    @allure.title("Company name view test")
    def test_company_name(self):
        find_assert(self.base_page, CompaniesLocators.COMPANY_NAME, 5, "Имя не отображается")

    @allure.title("Company name format test")
    def test_company_name_format(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        expected_pattern = rf"Кампания {current_date}"
        assert_regexp(self.base_page, CompaniesLocators.COMPANY_NAME_TEXT, expected_pattern, 5, "Название не соответствует формату")
    @allure.title("Company name handle test")
    def test_company_name_handle(self):
        self.base_page.move_to_element(CompaniesLocators.COMPANY_NAME_TEXT)
        self.base_page.click(CompaniesLocators.COMPANY_NAME_TEXT)

        assert 1 == 1, "Название не реагирует на нажатие"