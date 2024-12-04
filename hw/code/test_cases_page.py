import allure

from hw.code.cases_case_vk import CasesCaseVkAd
from hw.code.ui.locators.vk_ad_cases_locators import CasesLocators


@allure.story("Cases page")
class TestCasesCaseVkAd(CasesCaseVkAd):
    @allure.title("Cases view page Test")
    def test_cases_page(self):

        assert self.cases_page.get_text(CasesLocators.CASES_HEADER) == 'Кейсы', "Неверное отображение страницы"
