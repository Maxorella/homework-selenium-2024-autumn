import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_education_locators import EducationLocators


@allure.story("Проверка обучения")
class TestEducation(BaseCaseVkAd):
    authorize = True

    @allure.title("Popup test")
    def test_popup(self):
        self.base_page.click(EducationLocators.COMPANIES_HREF)

        assert self.base_page.find(EducationLocators.EDUCATION_POPAP).is_displayed(), "Не отображается подсказка"
