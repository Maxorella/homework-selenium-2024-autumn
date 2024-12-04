import allure
from selenium.webdriver.common.by import By

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_main_locators import MainPageNoLoginCases


@allure.story("Cases TestCase")
class TestCases(BaseCaseVkAd):

    authorize = False
    @allure.title("Company cases view Test")
    def test_company_cases(self):
        cases = self.base_page.find(MainPageNoLoginCases.CASES_CONTAINER)
        header = cases.find_element(By.TAG_NAME, 'h2')
        cases_examples = cases.find_element(*MainPageNoLoginCases.CASES_EXAMPLES)
        href = cases.find_element(By.TAG_NAME, 'a')
        assert (header.text == 'Кейсы компаний' and cases_examples.is_displayed() and href.is_displayed() ), "Кейсы компаний не отображаются корректно"

    @allure.title("Transfer to company cases page Test")
    def test_company_cases_page(self):
        current_window = self.driver.current_window_handle
        self.base_page.click(MainPageNoLoginCases.CASES_HREF)
        with self.switch_to_window(current_window):
            assert self.base_page.is_opened('https://ads.vk.com/cases',len('https://ads.vk.com/cases')), "Переход не произошел"

    @allure.title("Transfer to chosen case")
    def test_chosen_case(self):
        case = self.base_page.find(MainPageNoLoginCases.CHOSEN_CASE)
        title = case.find_element(*MainPageNoLoginCases.CASE_TITLE).text
        case.click()
        header = self.base_page.find(MainPageNoLoginCases.CASE_PAGE_TITLE)
        new_title = header.find_element(By.TAG_NAME, 'h1').text

        assert title == new_title, "Переход не на ту страницу"