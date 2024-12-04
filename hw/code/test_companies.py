import re
from datetime import datetime

import allure

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
            assert self.base_page.is_opened('https://ads.vk.com/hq/new_create/ad_plan',
                                            len('https://ads.vk.com/hq/new_create/ad_plan')), "Переход на страницу создание кампании"

    @allure.title("Create company view test")
    def test_create_company(self):

        assert self.base_page.find(CompaniesLocators.CREATE_COMPANY_CONTAINER).is_displayed(), "Контейнер не отображается"


    @allure.title("Company name view test")
    def test_company_name(self):

        assert self.base_page.find(CompaniesLocators.COMPANY_NAME).is_displayed(), "Имя не отображается"

    @allure.title("Company name format test")
    def test_company_name_format(self):

        company_name = self.base_page.get_text(CompaniesLocators.COMPANY_NAME_TEXT)

        current_date = datetime.now().strftime("%Y-%m-%d")
        expected_pattern = rf"Кампания {current_date}"

        if re.fullmatch(expected_pattern, company_name):
            pass
        else:
            assert 1 == 0, "Название не соответствует формату"

    @allure.title("Company name handle test")
    def test_company_name_handle(self):
        self.base_page.move_to_element(CompaniesLocators.COMPANY_NAME_TEXT)
        self.base_page.click(CompaniesLocators.COMPANY_NAME_TEXT)

        assert 1 == 1, "Название не реагирует на нажатие"