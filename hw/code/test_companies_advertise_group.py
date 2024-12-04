import allure

from hw.code.base_vk_ad import BaseCaseVkAd
from hw.code.ui.locators.vk_ad_companies_locators import GroupLocators


@allure.story("Группы объявлений")
class TestAdvertiseGroup(BaseCaseVkAd):
    authorize = True
    company = True

    @allure.title("Edit date")
    def test_edit_date(self):
        self.base_page.go_to_group()
        self.base_page.click(GroupLocators.SET_DATE)

        assert self.base_page.find(GroupLocators.CHOSE_DATES).is_displayed(), "Выбор даты не отображается"