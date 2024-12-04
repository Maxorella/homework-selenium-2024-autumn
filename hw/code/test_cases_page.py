import allure

from hw.code.asserts.asserts import *
from hw.code.cases_case_vk import CasesCaseVkAd
from hw.code.ui.locators.vk_ad_cases_locators import CasesLocators


@allure.story("Cases page")
class TestCasesCaseVkAd(CasesCaseVkAd):
    @allure.title("Cases view page Test")
    def test_cases_page(self):
        assert_compare_block_text(self.cases_page, CasesLocators.CASES_HEADER, 'Кейсы',
                                         10, "Неверное отображение страницы")